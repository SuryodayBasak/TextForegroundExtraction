# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:23:52 2015

@author: suryo
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

kernel1 = np.ones((5,5),np.uint8)
kernel2 = np.ones((3,3),np.uint8)

#img = cv2.imread('/home/suryo/Image_Processing_Exercises/resources/1.jpg',0)
#img = cv2.imread('/home/suryo/Image_Processing_Exercises/resources/1.jpg',0)

img = cv2.imread('/home/suryo/Image_Processing_Exercises/resources/book2/o8.jpg',0)
cv2.imshow('original', img)

"""
"""

clahen = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1n = clahen.apply(img)
cv2.imshow('cl1n', cl1n)

blur=cv2.medianBlur(img,5)

mask1 = np.zeros(img.shape[:2],np.uint8)
mask1 = (255-mask1)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(blur)
cv2.imshow('cl1', cl1)

circles_mask = cv2.dilate(cl1,kernel1,iterations = 4)
circles_mask = (255-circles_mask)
cv2.imshow('circles_mask', circles_mask)
thresh = 1
circles_mask = cv2.threshold(circles_mask, thresh, 255, cv2.THRESH_BINARY)[1]

edges = cv2.Canny(cl1,100,200)
cv2.imshow('edges', edges)

dilation = cv2.dilate(edges,kernel1,iterations = 1)
cv2.imshow('dilation', dilation)

display = cv2.bitwise_and(img,img,mask=dilation) 
cv2.imshow('display', display)
#cv2.imwrite('result3.jpg',display)

erosion = cv2.erode(display,kernel2,iterations = 1)
cv2.imshow('erosion', erosion)

"""
display2 = cv2.bitwise_xnor(display,display,mask=mask1) 
cv2.imshow('display2', display2)
cv2.imshow('mask', mask1)
"""

inv = (255-display)
cv2.imshow('inv', inv)

ret3,th1 = cv2.threshold(inv,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('inv2', th1)

display2 = cv2.bitwise_and(display,display,mask=th1) 
cv2.imshow('display2', display2)

ret3,th2 = cv2.threshold(display2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('prefinal', th2)

dilation2 = cv2.dilate(th2,kernel2,iterations = 1)
cv2.imshow('final', dilation2)

blur2=cv2.medianBlur(dilation2,3)
cv2.imshow('blur2', blur2)

#cv2.imwrite('result4.jpg',blur2)

anding = cv2.bitwise_and(img,img,mask=blur2) 
cv2.imshow('anding', anding)
#cv2.imwrite('result5.jpg',anding)

ret3,th3 = cv2.threshold(anding,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('otsu3', th3)

inv3 = (255-th3)
cv2.imshow('inv3', inv3)

anding2 = cv2.bitwise_and(blur2,blur2,mask=inv3) 
#cv2.imshow('anding2', anding2)

#pre_the_final_thing = cv2.bitwise_and(anding2,anding2,mask=circles_mask) 
anding2 = cv2.bitwise_and(anding2,anding2,mask=circles_mask) 
cv2.imshow('anding2', anding2)

dilation3 = cv2.dilate(anding2,kernel2,iterations = 1)
the_final_thing = (255-dilation3)

anding2 = 255-anding2
the_final_thing=cv2.medianBlur(the_final_thing,1)
cv2.imshow('the_final_thing', the_final_thing)
#cv2.imwrite('final_result2.jpg',the_final_thing)

cv2.imwrite('compare_res_1.jpg',anding2)
cv2.imwrite('compare_res_2.jpg',the_final_thing)

cv2.imshow('circles_mask', circles_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()