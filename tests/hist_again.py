# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:40:28 2015

@author: suryo
"""

import numpy as np
import cv2
kernel = np.ones((3,2),np.uint8)

image = cv2.imread('/home/suryo/Image_Processing_Exercises/resources/1.jpg',0)
cv2.imshow('image1',image)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(16,16))
cl1 = clahe.apply(image)

cv2.imshow('cl1', cl1)


clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl2 = clahe.apply(cl1)

cv2.imshow('cl2', cl2)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4,4))
cl3 = clahe.apply(cl2)

cv2.imshow('cl3', cl3)



cv2.waitKey(0)
cv2.destroyAllWindows()