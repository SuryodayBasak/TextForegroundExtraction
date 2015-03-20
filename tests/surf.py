# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 23:09:13 2015

@author: suryo
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/suryo/Image_Processing_Exercises/resources/1.jpg',0)

#surf = cv2.CV_SURF(400)

surf = cv2.xfeatures2d.SIFT(400)

kp, des = surf.detectAndCompute(img,None)

print len(kp)

cv2.waitKey(0)
cv2.destroyAllWindows()