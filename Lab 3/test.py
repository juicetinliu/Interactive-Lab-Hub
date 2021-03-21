import time, math, random
import subprocess
import digitalio
import board, busio, keyboard
import qwiic_twist
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
font_time = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 46)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Create bus object using the board's I2C port
i2c = busio.I2C(board.SCL, board.SDA)

twist = qwiic_twist.QwiicTwist()
twist.begin()

raindrops = []
drop = False
drop_size = 2
last_time = time.time()

add_flames = False
add_ices = False
start_voice = False
flames = []
ices = []
flame_time = time.time()
ice_time = time.time()

class Flame:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.v = 6
        self.ang = random.random() * 2 * math.pi
        self.remove = False
        self.col = "#FF"+ ''.join([random.choice('02468BDF') for j in range(2)]) + "00" #random red-yellow

    def draw(self, canvas):
        x, y = self.x, self.y
        #canvas.text((self.x, self.y), self.symb, font=font)
        canvas.point([x, y], fill=self.col)

    def move(self):
        vel = self.v
        self.ang = 3*math.pi/2 + (random.random() - 0.5) * 2 * (math.pi / 8)
        self.x += vel * math.cos(self.ang)
        self.y += vel * math.sin(self.ang)
        if(self.x > width or self.x < 0 or self.y > height or self.y < 0):
            self.remove = True
        
class Ice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.v = 2
        self.ang = random.random() * 2 * math.pi
        self.symb = "❄"
        self.remove = False

    def draw(self, canvas):
        x, y = self.x, self.y
        canvas.text((self.x, self.y), self.symb, font=font, fill="#FFFFFF")

    def move(self):
        vel = self.v
        self.ang = math.pi/2 + (random.random() - 0.5) * 2 * (math.pi / 2)
        self.x += vel * math.cos(self.ang)
        self.y += vel * math.sin(self.ang)
        if(self.x > width or self.x < 0 or self.y > height or self.y < 0):
            self.remove = True

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill="#391c3e")
    
    start_voice = twist.pressed

    if start_voice:
        twist.set_color(10, 100, 10)
        if keyboard.is_pressed('h'):
            add_flames = True
            add_ices = False
        elif keyboard.is_pressed('c'):
            add_flames = False
            add_ices = True
        else:
            add_flames = False
            add_ices = False        
    elif add_flames:
        twist.set_color(100, random.randrange(100), 00)
        draw.rectangle((0, 0, width, height), outline=0, fill="#391c1c")
        if time.time() - flame_time > 0.01:
            flame_time = time.time()
            flames.append(Flame(random.randrange(width), height))
            flames.append(Flame(random.randrange(width), height))
            flames.append(Flame(random.randrange(width), height))
    elif add_ices:
        draw.rectangle((0, 0, width, height), outline=0, fill="#2e2e4c")
        twist.set_color(10, 10, 100)
        if time.time() - ice_time > 1:
            ice_time = time.time()
            ices.append(Ice(random.randrange(width), 0))
    else:
        twist.set_color(100, 10, 100)

    # Draw flames
    for f in flames:
        f.move()
        f.draw(draw)
    
    # Draw ices
    for i in ices:
        i.move()
        i.draw(draw)
        
    # Kill flames
    for f in reversed(flames):
        if f.remove:
            flames.remove(f)
        
    # Kill ices
    for i in reversed(ices):
        if i.remove:
            ices.remove(i)
    
    # print(twist.count)

    # Display image.
    disp.image(image, rotation)
    time.sleep(0.05)
