#!/usr/bin/env python3
# Reads four input buttons to light four corresponding LEDs

# Import PyBBIO library:
import Adafruit_BBIO.GPIO as GPIO
import time

#Setup the array
leds = ["GP1_3", "GP1_4", "RED", "GREEN"]
buttons = ["GP0_3", "GP0_4", "GP0_5", "GP0_6"]

#Button Event Handler
def updateLED(channel):
    print("channel = " + channel)
    state = GPIO.input(channel)
    GPIO.output(map[channel], state)
    print(map[channel] + " Toggled")
  
#Dictionary to hold button/led pairs
map = {}
    
#For loop to set up the button/leds
for x in range (0, 4) :
    GPIO.setup(leds[x],    GPIO.OUT)
    GPIO.setup(buttons[x], GPIO.IN)
    GPIO.output(leds[x], 1)
    map[buttons[x]] = leds[x]
    GPIO.add_event_detect(buttons[x], GPIO.BOTH, callback=updateLED)
    

print("Running...")

#Loop until program exits
try:
    while True:
        time.sleep(100)   # Let other processes run

except KeyboardInterrupt:
    print("Cleaning Up")
    GPIO.cleanup()
GPIO.cleanup()