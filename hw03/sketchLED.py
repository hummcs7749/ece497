#!/usr/bin/env python3
# Write an 8x8 Red/Green LED matrix
# https://www.adafruit.com/product/902

import Adafruit_BBIO.GPIO as GPIO
import smbus
import time
bus = smbus.SMBus(1)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

delay = 1; # Delay between images in s

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

col = [0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01]
grid = {} 
width = 8
height = 8
persist = 0
x = 0
y = 0
bounce = 0.3

#Button Events to move directionally
def btnUp(channel):
  global y 
  if(y > 0) :
    y = y - 1
    grid[y, x] = 1
    printGrid()
    time.sleep(bounce)
        
def btnRight(channel):
  global x 
  if(x < width - 1) :
    x = x + 1
    grid[y, x] = 1
    printGrid()
    time.sleep(bounce)

def btnLeft(channel):
  global x 
  if(x > 0) :
    x = x - 1
    grid[y, x] = 1
    printGrid()
    time.sleep(bounce)
        
def btnDown(channel):
  global y 
  if(y < height - 1) :
    y = y + 1
    grid[y, x] = 1
    printGrid()
    time.sleep(bounce)
    
#Button Event triggered by PAUSE to clear the board
def btnClear(channel):
  for i in range (0, width) :
    for j in range (0, width) :
      grid[i, j] = 0
  printGrid()
  
#Button Event triggered by MODE to quit
def btnQuit(channel):
  quit()

for i in range (0, width) :
    for j in range (0, height) :
        grid[i,j] = 0

def printGrid():
    temp = 0b00000000
    current = 0
    for i in range (0, height) :
        for j in range (0, width) :
            if(grid[i,j] == 1) :
                current = 0b00000001 << j 
                temp = current | temp
        col[i] = temp;
        temp = 0;
    outPut = [0x00, col[0], 0x00, col[1], 0x00, col[2], 0x00, col[3],
    0x00, col[4], 0x00, col[5], 0x00, col[6], 0x00, col[7]]
    bus.write_i2c_block_data(matrix, 0, outPut)

#Sets arrays of buttons and accompanying methods
buttons = ["GP0_3", "GP0_4", "GP0_5", "GP0_6", "PAUSE", "MODE"]
commands = [btnRight, btnLeft, btnDown, btnUp, btnClear, btnQuit]

#For loop to set up the buttons
for i in range (0, 6) :
    GPIO.setup(buttons[i], GPIO.IN)
    GPIO.add_event_detect(buttons[i], GPIO.RISING, callback=commands[i])

grid[0,0] = 1;
printGrid()
print("")

#Loop to be used for keyboard commands
while(persist == 0) :
    printGrid()
    #Takes input for keyboard commands
    inp = input("")
    if(inp == 'w') :
      if(y > 0) :
        y = y - 1
        grid[y, x] = 1

    if(inp == 's') :
      if(y < height - 1) :
        y = y + 1
        grid[y, x] = 1

    if(inp == 'a') :
      if(x > 0) :
        x = x - 1
        grid[y, x] = 1

    if(inp == 'd') :
      if(x < width - 1) :
        x = x + 1
        grid[y, x] = 1

    if(inp == 'c') :
        for i in range (0, width) :
            for j in range (0, width) :
                grid[i, j] = 0;

    if(inp == 'x') :
      persist = 1
