# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:24:29 2015

@author: suryo
"""

import cv2
import prep

img = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/Kandanu10.jpg',0)
cv2.imshow('Output',prep.preprocess(img))

cv2.waitKey(0)
cv2.destroyAllWindows()

