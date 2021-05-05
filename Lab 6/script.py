import time
import board
import busio
import adafruit_mpu6050
import socket

import signal
import sys
from queue import Queue

 
i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

thresh = 15
run_avg = []
run_avg_len = 10

peak_neighbors = [(0,0,0), (0,0,0)]

print("1 - Threshold Detection / 2 - Averaging / 3 - Peak Detection")
mode = int(input())
while int(mode) not in [1, 2, 3]:
    print("Please enter 1, 2 or 3")
    mode = int(input())

while True:
    accel = mpu.acceleration
    x, y, z = accel
    if mode == 1:
        #Threshold detection
        passedthresh = []
        for i in range(3):
            if accel[i] > thresh:
                passedthresh.append(i)
        print("Shook in " + "".join([["x", "y", "z"][p] for p in passedthresh]))
        
        if max(abs(x), abs(y), abs(z)) > thresh:
            print("SHOOK?")
        else:
            print("Kalm")
    elif mode == 2:
        #Averaging
        run_avg.append((x, y, z))
        if len(run_avg) > run_avg_len:
            run_avg.pop(0)
        
        output = [0, 0, 0]
        for x,y,z in run_avg:
            output[0] += x
            output[1] += y
            output[2] += z
        output = [o / run_avg_len for o in output]
        print(output, len(run_avg))
    elif mode == 3:
        peak_neighbors.append((x, y, z))
        peaked = []
        for i in range(3):
            if peak_neighbors[1][i] > peak_neighbors[0][i] and peak_neighbors[1][i] > peak_neighbors[2][i]:
                peaked.append(i)
        print("Peak in " + "".join([["x", "y", "z"][p] for p in peaked]))
        if len(peak_neighbors) > 2:
            peak_neighbors.pop(0)
    
    