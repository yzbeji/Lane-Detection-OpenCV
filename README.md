# Lane-Detection-OpenCV
![](https://github.com/yzbeji/Lane-Detection-OpenCV/blob/main/lane-detection%20.gif)

This is a pretty cool project that involves lane detection when driving on the road. I used OpenCV library (in Python) which is one of the biggest libraries for Image Manipulation and Computer Vision. This code is free to use, just copy it in your IDE and also download the original video from SOURCES file and run it. Short explanation: 
 - The video is made from more images (frames)
 - We select an area where we are interested to check if there are any white lines (trapezoid)
 - Every frame will be grayscaled and applied Gaussian Blur to it to smooth it and reduce noise
 - After the step from above, a new gradient image will created
 - Using Hough Lines on the last image the lines are being drawn on the original image
 - The magic happens. Finally!
