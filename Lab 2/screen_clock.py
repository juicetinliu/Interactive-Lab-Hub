import time, math, random
import subprocess
import digitalio
import board
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

wavepos = height
num_points = int(width/4)
wave = [0 for i in range(num_points)]
wave_v = [0 for i in range(num_points)]

raindrops = []
drop = False
drop_size = 2
last_time = time.time()

fill_tub = False
fill_x = int(num_points * 0.85)
drain_tub = False
drain_x = int(num_points * 0.15)

add_fish = True

class Fish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symb = "🐟𓆜🐠"
        self.v = 1
        self.ang = random.random() * 2 * math.pi

    def draw(self, canvas):
        canvas.text((self.x, self.y), self.symb, font=font)

    def move(self):
        if self.y < wavepos:
            self.y += 1
        else:
            self.ang += (random.random() - 0.5) * 2 * (math.pi / 8)
            self.x += self.v * math.cos(self.ang)
            self.y += self.v * math.sin(self.ang)
        

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill="#391c3e")
    draw.rectangle((width/4, height/6, width*3/4, height/3), fill="#FFFFFF")
    
    # OTHER DRAWING AND LOGIC
    if not (buttonB.value or buttonA.value):
        fill_tub = False
        drain_tub = False
        add_fish = True
    else:
        add_fish = False
        fill_tub = not buttonA.value and wavepos > 0
        drain_tub = not buttonB.value and wavepos < height
    
    # Release droplet every second
    if time.time() - last_time > 1 and wavepos > 0:
        last_time = time.time()
        raindrops.append([random.randrange(1,num_points-1), 0])
        drop = False
    
    # Move droplets and calculate collision with water surface
    for r in range(len(raindrops)-1, -1, -1):
        rd = raindrops[r]
        rd[1] += 10
        if rd[1] >= wave[rd[0]] + wavepos:
            raindrops.pop(r)
            wavepos -= 1
            wave[rd[0]] = -10
    
    # Draw droplets       
    for r in raindrops:
        rx = (r[0]-1)*width/(num_points-2)
        ry = r[1]
        draw.ellipse([rx-drop_size, ry-drop_size, rx+drop_size, ry+drop_size], fill="#00FFFF")
    
    # Propagate wave
    for w in range(1, num_points-1):
        wave[w] = ((wave_v[w-1] + wave_v[w+1]) >> 1) - wave[w]
        wave[w] -= wave[w] >> 3
    
    # Fill tub
    if fill_tub:
        fill_tub_x = (fill_x-1)*width/(num_points-2)
        draw.rectangle([fill_tub_x - 5, 0, fill_tub_x + 5, height], fill="#00FFFF")
        wave[fill_x] = 10 + int(5*math.sin(time.time()))
        wavepos -= 0.5
        
    # Drain tub
    if drain_tub:
        wave[drain_x] = 10 + int(5*math.sin(time.time()))
        wavepos += 0.5
        
    # Draw water
    line_points = [((i-1)*width/(num_points-2), w + wavepos) for i, w in enumerate(wave)]
    draw.polygon(line_points+[(width,height),(0,height)], fill="#00FFFF")
    temp = wave_v
    wave_v = wave
    wave = temp
    
    # DRAW TIME ON TOP (LAST STEP)
    system_time = time.strftime("%b/%d/%Y %H:%M:%S")
    date_str, time_str = system_time.split(" ")
    
    date_print = " ".join(date_str.split("/"))
    date_font = font.getsize(date_print)
    x = width/2 - date_font[0]/2
    y = height/4 - date_font[1]/2
    draw.text((x, y), date_print, font=font, fill="#0373fc")

    time_font = font_time.getsize(time_str)
    x_start = width/2 - time_font[0]/2
    y_start = wavepos - time_font[1]
    for t in time_str:
        d_w = font_time.getsize(t)
        cx = x_start
        x_start += d_w[0]
        cy = wave[int((cx+d_w[0]/2)*num_points/width)] + y_start
        col = '#FF8040' if t == ':' else '#FFFF00'
        draw.text((cx, cy), t, font=font_time, fill=col)
    
    # Display image.
    disp.image(image, rotation)
    time.sleep(0.01)