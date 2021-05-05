import board
import busio
import adafruit_mpu6050
import time
import paho.mqtt.client as mqtt
import uuid
import signal

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

print("Player 1 or 2?")
p = -1
while p not in [1, 2]:
    p = int(input())
    print("Please enter 1 or 2")

topic = 'IDD/juicey/labyrinth/' + ('X' if p == 1 else 'Y')
p -= 1

def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(topic)

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')
client.on_connect = on_connect

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

client.loop_start()

# this lets us exit gracefully (close the connection to the broker)
def handler(signum, frame):
    print('exit gracefully')
    client.loop_stop()
    exit (0)

# hen sigint happens, do the handler callback function
signal.signal(signal.SIGINT, handler)

# our main loop
while True:
    accel = mpu.acceleration
    
    client.publish(topic, f"{accel[p]}")
    
    time.sleep(.01)
    