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
gcc sketch.c -g -Wall -c -ansi
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

