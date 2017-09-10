#!/usr/bin/env python3
# Reads the PAUSE button using interupts and sets the LED
# Pin table at https://github.com/beagleboard/beaglebone-blue/blob/master/BeagleBone_Blue_Pin_Table.csv

# Import PyBBIO library:
import Adafruit_BBIO.GPIO as GPIO
import time

button1="PAUSE"  
button2="GP0_4"
button3="MODE"  
button4="GP0_6"

LED1   ="GP1_3"
LED2   ="GP1_4"
LED3   ="RED"
LED4   ="GREEN"


# Set the GPIO pins:
GPIO.setup(LED1,    GPIO.OUT)
GPIO.setup(LED2,    GPIO.OUT)
GPIO.setup(LED3,    GPIO.OUT)
GPIO.setup(LED4,    GPIO.OUT)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button4, GPIO.IN)

GPIO.output(LED1, 1)
GPIO.output(LED2, 1)
GPIO.output(LED3, 1)
GPIO.output(LED4, 1)

print("Running..")

GPIO.add_event_detect(button1, GPIO.BOTH) # RISING, FALLING or BOTH
GPIO.add_event_detect(button2, GPIO.BOTH)
GPIO.add_event_detect(button3, GPIO.BOTH)
GPIO.add_event_detect(button4, GPIO.BOTH)


while True:   # This is ugly since we have to poll for the event
  if GPIO.event_detected(button1):
    print("Note")
    state = GPIO.input(button1)
    GPIO.output(LED1, state)
    print(LED1 + " Toggled")
    
  if GPIO.event_detected(button2):
    print("Note")
    state = GPIO.input(button2)
    GPIO.output(LED2, state)
    print(LED2 + " Toggled")
    
  if GPIO.event_detected(button3):
    print("Note")
    state = GPIO.input(button3)
    GPIO.output(LED3, state)
    print(LED3 + " Toggled")
    
  if GPIO.event_detected(button4):
    print("Note")
    state = GPIO.input(button4)
    GPIO.output(LED4, state)
    print(LED4 + " Toggled")
