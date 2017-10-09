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

Etch-a-sketch has also been updated so that it now prompts the user for a 
character, 'R', 'B', or 'G', to set the color of the line drawn to, defaulting to 
brown if none of those characters are input. The line width has also been updated 
to five pixels. 