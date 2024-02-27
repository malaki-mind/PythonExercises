# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:00:16 2024

As part of an exercise in Ardit Sulce's Udemy Python MegaCourse

The instructor asked students to resize a batch of images to 100x100 resolution

This is the result of the exercize without looking at the solution.

I had to figure out how to use the glob library to read batch of files in dir
"""

import glob
import cv2

count = 0

for file in glob.glob("*.jpg"):
    print(file)
    image = cv2.imread(file,1)
    img_resize = cv2.resize(image,(100,100))
    cv2.imwrite("image" + str(count) + ".jpg",img_resize)
    count+=1   
 
        
      
        

