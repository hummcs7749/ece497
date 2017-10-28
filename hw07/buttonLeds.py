#!/usr/bin/env python3
# Reads the PAUSE button using interupts and sets the LED
# Pin table at https://github.com/beagleboard/beaglebone-blue/blob/master/BeagleBone_Blue_Pin_Table.csv

# Import PyBBIO library:
import Adafruit_BBIO.GPIO as GPIO
import time

button1="GP1_3"  


LED1   ="GP1_4"

# Set the GPIO pins:
GPIO.setup(LED1,    GPIO.OUT)
GPIO.setup(button1, GPIO.IN)


GPIO.output(LED1, 1)


# print("Running..")

GPIO.add_event_detect(button1, GPIO.BOTH) # RISING, FALLING or BOTH



while True:   # This is ugly since we have to poll for the event
  if GPIO.event_detected(button1):
    # print("Note")
    state = GPIO.input(button1)
    GPIO.output(LED1, state)
    # print(LED1 + " Toggled")

    

