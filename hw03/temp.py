#!/usr/bin/env python3
# Read a TMP101 sensor
# sudo apt install python3-smbus

import Adafruit_BBIO.GPIO as GPIO
import smbus
import time

#Setup the array
switch = ["GP1_3", "GP1_4"]
leds = ["RED", "GREEN"]

#Button Event Handler
def updateLED(channel):
    state = GPIO.input(channel)
    GPIO.output(map[channel], state)
    print("%dF" %(tMap[channel]))
  
#Dictionary to hold button/led pairs
map = {}
temp = [0, 0]
tMap = {}
    
#For loop to set up the button/leds
for x in range (0, 2) :
    GPIO.setup(leds[x],    GPIO.OUT)
    GPIO.setup(switch[x], GPIO.IN)
    GPIO.output(leds[x], 1)
    map[switch[x]] = leds[x]
    tMap[switch[x]] = temp[x]
    GPIO.add_event_detect(switch[x], GPIO.BOTH, callback=updateLED)

bus = smbus.SMBus(1)
address = 0x48
address2 = 0x4a
bus.write_byte_data(address, 3, 0x1c)
bus.write_byte_data(address2, 3, 0x1a)

while True:
    temp[0] = bus.read_byte_data(address, 0)
    temp[1] = bus.read_byte_data(address2, 0)
    
    tMap[switch[0]] = temp[0] * 9/5 + 32
    tMap[switch[1]] = temp[1] * 9/5 + 32
    time.sleep(0.25)
    