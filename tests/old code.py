# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:31:26 2015

@author: suryo
"""

import numpy as np
import cv2

image = cv2.imread('/home/suryo/Image_Processing_Exercises/resources/leaf3.jpg')
#image = cv2.imread('/home/suryo/IMED/Project1/Images/testcase3',0)



image=cv2.medianBlur(image,3)
resized = image.copy()
edges = cv2.Canny(resized,100,200)

ret,thresh = cv2.threshold(edges,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
M = cv2.moments(cnt)
print M

for xx in contours:
    cv2.drawContours(edges,[xx],-1,(255,255,255),-1)


#cv2.fillPoly(resized, pts =contours, color=(255,255,255))


kernel = np.ones((5,5),np.uint8)


dilation = cv2.dilate(edges,kernel,iterations = 1)
erosion = cv2.erode(dilation,kernel,iterations = 1)

dilation = cv2.dilate(erosion,kernel,iterations = 1)
erosion = cv2.erode(dilation,kernel,iterations = 1)

dilation = cv2.dilate(erosion,kernel,iterations = 1)
erosion = cv2.erode(dilation,kernel,iterations = 2)


closing = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, kernel)
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

final1=opening.copy()
final2=cv2.medianBlur(final1,31)


ret,thresh = cv2.threshold(final2,127,255,0)
contours2, hierarchy2 = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


"""
for i in contours2:
    (x,y),radius = cv2.minEnclosingCircle(i)
    center = (int(x),int(y))
    radius = int(radius)
    print x
    print y
    print radius
    print " "
    
    cv2.circle(resized1,center,radius,(0,0,255),2)   
"""
    
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.imshow('img', thresh)
#img is an identifier that makes sure that you access the resizable window

cv2.waitKey(0)
cv2.destroyAllWindows()