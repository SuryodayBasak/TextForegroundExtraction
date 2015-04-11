# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:08:52 2015

@author: suryo
"""

import cv2
import binarization
import numpy as np
kernel = np.ones((5,5),np.uint8)

img = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/Kandanu10.jpg',0)
cv2.imshow('original', img)
mask = np.zeros(img.shape[:2],np.uint8)

binary = binarization.binary_img(img)
cv2.imshow('binary', binary)

#contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt=contours[max_index]

print max_index

cv2.drawContours(mask, contours, max_index-1, (0,255,0), 3)
cv2.imshow('largest', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()