# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:35:31 2015

@author: suryo
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt

kernel1 = np.ones((5,5),np.uint8)
kernel2 = np.ones((3,3),np.uint8)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

#img = cv2.imread('/home/suryo/Image_Processing_Exercises/resources/1.jpg',0)
#img = cv2.imread('/home/suryo/Image_Processing_Exercises/resources/book2/o8.jpg',0)

img = cv2.imread('/home/suryo/Image_Processing_Exercises/resources/1.jpg',0)
cv2.imshow('original', img)

img_dilate = cv2.dilate(img,kernel1,iterations = 3)
cv2.imshow('img_erode', img_dilate)

inv = 255 - img_dilate
cv2.imshow('inv', inv)

thresh = 1
noise_mask = cv2.threshold(inv, thresh, 255, cv2.THRESH_BINARY)[1]

cv2.imshow('noise_mask', noise_mask)
"""
thresh = 1
noise_mask = cv2.threshold(inv, thresh, 255, cv2.THRESH_BINARY)[1]

noise_mask = cv2.adaptiveThreshold(inv,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
cv2.imshow('noise_mask', noise_mask)
"""

cv2.waitKey(0)
cv2.destroyAllWindows()
