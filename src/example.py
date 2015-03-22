# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:07:06 2015

@author: suryo
"""

import cv2
import binarization

img = cv2.imread('/home/suryo/Image_Processing_Exercises/resources/book2/o8.jpg',0)
binary = binarization.binary_img(img)
cv2.imshow('binary', binary)

cv2.waitKey(0)
cv2.destroyAllWindows()