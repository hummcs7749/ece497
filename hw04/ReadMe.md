Memory Map
A memory map of the BeagleBone is enclosed in the excel sheet, 
BeagleBoneMemory.ods. 

GPIO via mmap
The solution to this problem is in mmapTest.c. One can use GPIO1_17 and 
GPIO3_17 connected pushbuttons to flash the USR2 and USR3 Leds. This program 
needs to be run with sudo. 

Etch a Sketch with Rotary Encoders 
The solution to this problem is in rotSketch.py. The position of the encoders 
is printed out, just as in encoder.py, and the encoders can be used to move the
cursor position on the x and y plane respectivley. Note, the degree  of the turn
does not matter, only that the encoder was turned in a given time period. This 
program needs to be run with sudo. 