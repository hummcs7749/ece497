Contained within this folder is the solution for homework six

The boris_education.png image can be displayed by running ./on.sh followed by 
rotate.sh. The roatation of the image can be controlled by editing rotate.sh, 
sepcifically the line-

modprobe fbtft_device name=adafruit28 busnum=1 rotate=180 gpios=reset:113,dc:116 cs=0

Replace the rotate = 180 with the desired value. 

The RedsNightmare can be played with-
mplayer -vf rotate=1 RedsNightmare.mpg

Where the value of rotate determines the rotation. 
1-Upright
2-Upside Down
3-Mirrored
4-Sideways (left top)
8-Upside Down Mirrored 

Text can be displayed with myText.sh, shown in whatever rotation the device 
is currently set to (It looks best in the 270 and 90 rotation, I suggest using
the rotate.sh function to set it thus)

Etch-a-sketch has also been updated so that it now accepts two arguemnts at the
command line, numbers for color and width. The command should look like this

sudo ./etch-a-sketch clr width

Where color is 1, 2, or three for the values Red, Green, and Blue respectivley.
If any other value is input, the color will defualt to brown.
and width is a number between 1 and 10, corresponding ot the desired line width. 
If a number below 1 is input, 1 is used for the width. If a number above 10 is 
input, 10 is used for the width. 
