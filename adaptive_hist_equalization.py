# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:24:03 2015

@author: suryo
"""

import numpy as np
import cv2

img = cv2.imread('/home/suryo/IMED/Project1/Images/IMG_20141112_080148.JPG',0)
blur = cv2.GaussianBlur(img[0:8,0:8],(5,5),0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(blur)


ret3,th3 = cv2.threshold(cl1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('img', th3)
cv2.waitKey(0)
cv2.destroyAllWindows()