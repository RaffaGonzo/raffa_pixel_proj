# raffa_pixel_proj
This program randomly destroys an image while maintaining general structure.

Here's how  it works
* first the user declares a path to the image they  would like to "destroy".
* next with the random library the program chooses three random boundaries between 0 and 255.
* then the destroy function is run on the image: this function consists of 3 for loops. These loops itterate through the 3D array that was created with the opencv library and change each of the values in the pixels. This function also randomly chooses which boundery to use from the 3 bounderies between 0 and 255. The bounderies are used in an math function that has a small amount of logic in it. For more info check out my code!

This program does require opencv and python 3.6
python 3.6 is easy enough to install but opencv can give people trouble. I use a mac so I can provide the link to the  install tutorial that worked for me. 

here is the link: https://www.swarthmore.edu/NatSci/mzucker1/e27_s2016/install_opencv.html
