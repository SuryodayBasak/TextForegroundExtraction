# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:03:59 2015

@author: suryo
"""

import cv2
import prep
kernel = np.ones((5,5),np.uint8)

img = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/1.jpg',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

sobely = cv2.erode(sobely,kernel,iterations = 1)
sobely = cv2.dilate(sobely,kernel,iterations = 1)

cv2.imshow('sobely', sobely)

sc = prep.skew_correction(sobely)

cv2.imshow('sc', sc)

cv2.waitKey(0)
cv2.destroyAllWindows()