# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:42:03 2015

@author: suryo
"""

import numpy as np
import cv2
kernel = np.ones((5,5),np.uint8)

image = cv2.imread('/home/suryo/Image_Processing_Exercises/resources/1.jpg',0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(image)
ret3,ot = cv2.threshold(cl1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(cl1,(5,5),0)

# create a CLAHE object (Arguments are optional).

cv2.imshow('img', image)
cv2.imshow('cl1', cl1)
cv2.imshow('blur', blur)
cv2.imshow('ot', ot)

#inverting ot

inv = (255-ot)
cv2.imshow('inv', inv)

edges = cv2.Canny(inv,100,200)

"""
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for xx in contours:
    cv2.drawContours(edges,[xx],-1,(255,255,255),-1)
"""

cv2.imshow('edges',edges)

cv2.waitKey(0)
cv2.destroyAllWindows()