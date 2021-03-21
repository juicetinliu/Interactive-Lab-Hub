import time, math, random
import subprocess
import digitalio
import board, busio
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

twist = QwiicTwist(i2c)  # default address is 0x3F

print(twist.count)

raindrops = []
drop = False
drop_size = 2
last_time = time.time()

add_flames = False
add_ices = False
flames = []
ices = []
flame_time = time.time()
ice_time = time.time()

class Flame:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.v = 1
        self.ang = random.random() * 2 * math.pi
        self.remove = False
        self.col = "#"+''.join([random.choice('789ABCDEF') for j in range(6)])

    def draw(self, canvas):
        x, y = self.x, self.y
        #canvas.text((self.x, self.y), self.symb, font=font)
        canvas.point([x, y], fill=self.col)

    def move(self):
        vel = self.v
        self.ang = 3*math.pi/2 + (random.random() - 0.5) * 2 * (math.pi / 16)
        self.x += vel * math.cos(self.ang)
        self.y += vel * math.sin(self.ang)
        if(self.x > width or self.x < 0 or self.y > height):
            self.remove = True
        

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill="#391c3e")
    draw.rectangle((width/4, height/6, width*3/4, height/3), fill="#CCCCCC")
    
    # # OTHER DRAWING AND LOGIC
    # fill_tub = not buttonA.value
    # drain_tub = not buttonB.value
    
    # # Release droplet every second
    # if add_flames:
    #     if time.time() - flame_time > 1:
    #         flame_time = time.time()

    # # Release droplet every second
    # if add_ices:
    #     if time.time() - ice_time > 1:
    #         ice_time = time.time()
    
    # # Draw flames
    # for f in flames:
    #     f.move()
    #     f.draw(draw)
        
    # # Kill flames
    # for f in reversed(flames):
    #     if f.remove:
    #         flames.remove(f)
    
    # # Draw ices
    # for i in ices:
    #     i.move()
    #     i.draw(draw)
        
    # # Kill ices
    # for i in reversed(ices):
    #     if i.remove:
    #         ices.remove(i)
    
    print(twist.count)

    # Display image.
    disp.image(image, rotation)
    time.sleep(0.01)