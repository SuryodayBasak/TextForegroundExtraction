# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 01:16:21 2015

@author: suryo
"""

import cv2
import numpy as np

lower_black = np.array([0,0,0])
upper_black = np.array([180,255,50])


img = cv2.imread('/home/suryo/Image_Processing_Exercises/resources/book2/o8.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv, lower_black, upper_black)


cv2.imshow('img', img)
cv2.imshow('mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()