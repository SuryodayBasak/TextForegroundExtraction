# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:41:19 2015

@author: suryo
"""

import cv2
import numpy as np
import binarization

kernel = np.ones((5,5),np.uint8)

img = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/Kandanu10.jpg',0)
img=cv2.medianBlur(img,5)
largest_contour = np.zeros(img.shape[:2],np.uint8)

sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

abs_sobel64f = np.absolute(sobely)
sobel_8u = np.uint8(abs_sobel64f)

#sobely = cv2.erode(sobely,kernel,iterations = 1)

cv2.imshow('sobely',sobel_8u)

#contours, hierarchy = cv2.findContours(sobely,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.waitKey(0)
cv2.destroyAllWindows()