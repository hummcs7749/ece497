I have completed all of steps one through six, broken down item by item 
as follows


1. Installing the latest shipped image on the BeagleBone
   My BeagleBone blue is operational with a flashed sd card
2. Setting up a host computer with Linux for kernel development
   My computer has a dual boot from when I took CSSE332, and thus had linux
already installed. 
3. Gathering all the needed SD cards, cables, etc.
   I have three SD cards, an SD card reader, a USB extender, and the bone 
itself. I have also checked out the lab kit from the parts room. 
   
4. Installing git on a your host
   I updated my git repository from my summer internship and have ready acess 
from my host computer and my BeagleBone
5. signing up for the two beagle Google groups (See Working With Open Source)
   I have viewed both check marks on the list and succesfully completed all 
accompanying git activiites. 
6. Writing a simple Etch-a-sketch program
   I have written a simple Etch-a-Sketch program as detailed below. 



Etch-a-sketch Notes
This directory contains the sketch.c file used to complete homework one. sketch.c
is called with the variables for height and width in the format

./a.out <height> <width>

After starting sketch.c, the user manipulates an etch a sketch with the following key strokes

w- moves up
s- moves down
a- moves left
d- moves right
c- clears
x- exits the program

One should press enter after every command in input. 

Example Compile/Run for an 8x8 board
gcc sketch.c 
./a.out 8 8

Sample Output

Welcome to BeagleSketch! Here are the rules
w -> Move Up
s -> Move Down
a -> Move Left
d -> Move Right
c -> Clear Board
x -> Exit Program
   0 1 2 3 4 5 6 7 
0: X               
1:                 
2:                 
3:                 
4:                 
5:                 
6:                 
7:                 
d
   0 1 2 3 4 5 6 7 
0: X X             
1:                 
2:                 
3:                 
4:                 
5:                 
6:                 
7:                 
s
   0 1 2 3 4 5 6 7 
0: X X             
1:   X             
2:                 
3:                 
4:                 
5:                 
6:                 
7:                 
d
   0 1 2 3 4 5 6 7 
0: X X             
1:   X X           
2:                 
3:                 
4:                 
5:                 
6:                 
7:                 
c
   0 1 2 3 4 5 6 7 
0:                 
1:                 
2:                 
3:                 
4:                 
5:                 
6:                 
7:                 
s
   0 1 2 3 4 5 6 7 
0:                 
1:                 
2:     X           
3:                 
4:                 
5:                 
6:                 
7:                 
a
   0 1 2 3 4 5 6 7 
0:                 
1:                 
2:   X X           
3:                 
4:                 
5:                 
6:                 
7:                 
x

// Comment from Prof. Yoder
// See README requirements
// C code work
// Grade:  7/10