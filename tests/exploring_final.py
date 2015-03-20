# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:49:43 2015

@author: suryo
"""

import numpy as np
import cv2
kernel = np.ones((3,2),np.uint8)

image = cv2.imread('/home/suryo/Image_Processing_Exercises/resources/1.jpg',0)
cv2.imshow('image1',image)

erosion = cv2.erode(image,kernel,iterations = 2)
cv2.imshow('erosion',erosion)

blur = cv2.GaussianBlur(erosion,(5,5),0)
cv2.imshow('blur',blur)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(blur)
cv2.imshow('cl1',cl1)

erosion2 = cv2.erode(cl1,kernel,iterations = 3)
cv2.imshow('erosion2',erosion2)

inv = (255-erosion2)
cv2.imshow('inv',inv)
cv2.imwrite('result1.jpg',inv)

cl2 = clahe.apply(inv)
cv2.imshow('cl2',cl2)

blur2 = cv2.GaussianBlur(cl2,(5,5),0)
cv2.imshow('blur2',blur2)

#opening = cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel, iterations = 2)
opening = cv2.morphologyEx(cl2,cv2.MORPH_OPEN,kernel, iterations = 2)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.cv.CV_DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

cv2.imwrite('result2.jpg',sure_fg)

cv2.imshow('fg',sure_fg)
"""
blur2 = cv2.GaussianBlur(inv,(5,5),0)
cv2.imshow('blur2',blur2)

gauss = cv2.adaptiveThreshold(blur2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
cv2.imshow('gauss',gauss)



display = cv2.bitwise_and(image, image, mask=inv)  
cv2.imshow('display',display)

cl2 = clahe.apply(erosion2)
cv2.imshow('cl2',cl2)


gauss = cv2.adaptiveThreshold(cl2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
cv2.imshow('gauss',gauss)


ret3,ot = cv2.threshold(erosion2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('ot',ot)

gauss = cv2.adaptiveThreshold(erosion,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
cv2.imshow('gauss',gauss)




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