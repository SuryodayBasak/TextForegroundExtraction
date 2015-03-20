# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:44:54 2015

@author: suryo
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('/home/suryo/Image_Processing_Exercises/resources/1.jpg',0)
cv2.imshow('image1',image)

blurred_frame=cv2.medianBlur(image,15)

plt.hist(blurred_frame.ravel(),256,[0,256]); plt.show()