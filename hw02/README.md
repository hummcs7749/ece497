# ece497
For fall quarter 2017

For Part One, run fourLights 
e.g.
./fourLights.py

This assumes four buttons connected to GP0_3 through GP0_6, which will toggle
on/off four LEDS connected to GP1_3, GP1_4, GREEN, and RED

Note, GP0_6 and GP0_4 are pull up switches, GP0_5 and GP0_3 are pull down 
switches. 


For Part Two, run sketcher.py, then give the dimensions of the grid to be used
e.g.
./sketcher.py
What is the width: 5
The width is 5
What is the height: 5
The height is 5
    0 1 2 3 4
0:
1:
2:
3:
4:

From there, input can be given with either the keyboard or the buttons. 

The Commands are as follows

Move Up: GP0_6/w
Move Down: GP0_5/s
Move Left: GP0_4/a
Move Right: GP0_3/d
Clear: PUASE/c
Quit: MODE/x

# Comments from Prof. Yoder
# Looks good. Nice documentation. 
# Grade:  10/10