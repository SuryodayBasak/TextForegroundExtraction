# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:24:29 2015

@author: suryo
"""

import cv2
import prep2

img = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/1.jpg',0)
cv2.imshow('Output',prep2.preprocess(img))

cv2.waitKey(0)
cv2.destroyAllWindows()

