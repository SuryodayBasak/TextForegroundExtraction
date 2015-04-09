# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:20:03 2015

@author: suryo
"""

import cv2
import binarization
import numpy as np
kernel = np.ones((5,5),np.uint8)

img = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/Kandanu10.jpg',0)
cv2.imshow('original', img)
binary = binarization.binary_img(img)
cv2.imshow('binary', binary)

dil = cv2.dilate(binary,kernel,iterations = 1)
cv2.imshow('dil', dil)

contours, hierarchy = cv2.findContours(dil,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# Find the index of the largest contour
areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt=contours[max_index]

print max_index
print cnt

x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(dil,(x,y),(x+w,y+h),(0,255,0),-1)

cv2.imshow('im', dil)

cv2.waitKey(0)
cv2.destroyAllWindows()