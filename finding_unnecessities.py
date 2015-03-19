# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:35:48 2015

@author: suryo
"""

import numpy as np
import cv2
kernel = np.ones((3,2),np.uint8)

image = cv2.imread('/home/suryo/Image_Processing_Exercises/resources/1.jpg',0)
cv2.imshow('image1',image)

blur = cv2.GaussianBlur(image,(5,5),0)

erosion = cv2.erode(blur,kernel,iterations = 2)

th3 = cv2.adaptiveThreshold(erosion,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

# create a CLAHE object (Arguments are optional).


#cv2.imshow('th3',th3)

th3_blur = cv2.GaussianBlur(th3,(5,5),0)

inv = (255-th3)
#cv2.imshow('inv', inv)








#display = cv2.bitwise_and(image, image, mask=inv)  
cv2.imshow('image2',th3)
cv2.imshow('inv',inv)

erosion2 = cv2.erode(inv,kernel,iterations = 3)
dilation2 = cv2.dilate(erosion2,kernel,iterations = 11)

cv2.imshow('inv2',dilation2)


display = cv2.bitwise_and(image, image, mask=dilation2)  
cv2.imshow('display',display)

"""
inv2 = (255-display)

cv2.imshow('inv2', inv2)


clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl2 = clahe.apply(inv2)

blur2 = cv2.GaussianBlur(cl2,(5,5),0)

th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

cv2.imshow('thrrr', th3)
           
inv = (255-th3)

cv2.imshow('invvv', inv)
"""

cv2.waitKey(0)
cv2.destroyAllWindows()