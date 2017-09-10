#!/usr/bin/env python3

# Import PyBBIO library:
import Adafruit_BBIO.GPIO as GPIO
import time

x = 0
y = 0
grid = {} 
persist = 0

def btnUp(channel):
    global y 
    if(y > 0) :
        y = y - 1
        grid[y, x] = "X"
        printGrid()

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
    
button1="PAUSE"  
button2="GP0_4"
button3="MODE"  
button4="GP0_6"

GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button4, GPIO.IN)


width = input("What is the width: ")
print("The width is " + width)
height = input("What is the height: ")
print("The height is " + height)

width = int(width)
height = int(height)


for i in range (0, width) :
    for j in range (0, height) :
        grid[i,j] = " "
        
for i in range (0, width) :
    for j in range (0, height) :
        print(grid[i,j], end = "")
    print("")

print("")



GPIO.add_event_detect(button1, GPIO.RISING, callback=btnUp)
#GPIO.add_event_detect(buttons[0], GPIO.BOTH, callback=updateLED)


while(persist == 0) :
    printGrid()
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
