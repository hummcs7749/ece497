#!/usr/bin/env python3

# Import PyBBIO library:
import Adafruit_BBIO.GPIO as GPIO
import time

#Global variable for position
x = 0
y = 0
#Global variable for the grid
grid = {} 
#Global Variable whether or not to continue
persist = 0


#Button Events to move directionally
def btnUp(channel):
  global y 
  if(y > 0) :
    y = y - 1
    grid[y, x] = "X"
    printGrid()
        
def btnRight(channel):
  global x 
  if(x < width - 1) :
    x = x + 1
    grid[y, x] = "X"
    printGrid()

def btnLeft(channel):
  global x 
  if(x > 0) :
    x = x - 1
    grid[y, x] = "X"
    printGrid()
        
def btnDown(channel):
  global y 
  if(y < height - 1) :
    y = y + 1
    grid[y, x] = "X"
    printGrid()
    
#Button Event triggered by PAUSE to clear the board
def btnClear(channel):
  for i in range (0, width) :
    for j in range (0, width) :
      grid[i, j] = " "
  printGrid()
  
#Button Event triggered by MODE to quit
def btnQuit(channel):
  quit()
        
#Method to print the grid
def printGrid():
  count = 0;
  print("    ", end = "")
  for i in range (0, width) :
    print("%d " %(count), end = "")
    count = count + 1
  print("")
  count = 0
  for i in range (0, height) :
    print("%d: " %(count), end = "")
    if(count < 10):
        print(" ", end = "")
    count = count + 1
    for j in range (0, height) :
      print("%s " %(grid[i,j]), end = "")
      temp = j/10
      while(temp >= 1):
        print(" ", end = "")
        temp = temp/10
    print("")
    
#Sets arrays of buttons and accompanying methods
buttons = ["GP0_3", "GP0_4", "GP0_5", "GP0_6", "PAUSE", "MODE"]
commands = [btnRight, btnLeft, btnDown, btnUp, btnClear, btnQuit]


#For loop to set up the buttons
for i in range (0, 6) :
    GPIO.setup(buttons[i], GPIO.IN)
    GPIO.add_event_detect(buttons[i], GPIO.RISING, callback=commands[i])

#User input to create grid
width = input("What is the width: ")
print("The width is " + width)
height = input("What is the height: ")
print("The height is " + height)

width = int(width)
height = int(height)

#Creates the grid
for i in range (0, width) :
    for j in range (0, height) :
        grid[i,j] = " "

#Loop to be used for keyboard commands
while(persist == 0) :
    printGrid()
    #Takes input for keyboard commands
    inp = input("")
    if(inp == 'w') :
      if(y > 0) :
        y = y - 1
        grid[y, x] = "X"

    if(inp == 's') :
      if(y < height - 1) :
        y = y + 1
        grid[y, x] = "X"

    if(inp == 'a') :
      if(x > 0) :
        x = x - 1
        grid[y, x] = "X"

    if(inp == 'd') :
      if(x < width - 1) :
        x = x + 1
        grid[y, x] = "X"

    if(inp == 'c') :
        for i in range (0, width) :
            for j in range (0, width) :
                grid[i, j] = " ";

    if(inp == 'x') :
      persist = 1
