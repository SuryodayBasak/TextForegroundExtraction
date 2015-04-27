# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:35:50 2015

@author: suryo
"""

import cv2
import binarization
import numpy as np
import time
kernel = np.ones((5,5),np.uint8)

img = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/1.jpg',0)
cv2.imshow('original', img)
all_angles = []

binary = binarization.binary_img(img)
#cv2.imshow('binary', binary)


contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#contours, hierarchy = cv2.findContours(binary.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)[0]
#print contours
#for c in contours:

print type(contours)
k = 0
areas = []
cnt = contours[0]
upper_bound=len(contours)
print upper_bound

for c in contours:
    areas.append(cv2.contourArea(c))
    
print areas
mean = np.mean(areas)
std_dev = np.std(areas)
print mean
print std_dev

dev_areas = []

for i in areas:
    dev_areas.append(i-std_dev)
    
print dev_areas
print dev_areas[0]

"""
for i in range(0,upper_bound):
    if(dev_areas[i]>0.0)
"""

dev_contours = np.zeros(img.shape[:2],np.uint8)
g = 0
for i in dev_areas:
    if((i>(-std_dev)) and (i<=(std_dev))):
        cv2.drawContours(dev_contours, contours, g, (255,255,255), -1)
        #print g
        g+=1
        #time.sleep(0.001)
print 'Done'

cv2.imshow('dev', dev_contours)
sobely = cv2.Sobel(dev_contours,cv2.CV_64F,0,1,ksize=5)
cv2.imshow('sobel', sobely)
abs_sobel64f = np.absolute(sobely)
sobel_8u = np.uint8(abs_sobel64f)

largest_contour = np.zeros(img.shape[:2],np.uint8)
#contours, hierarchy = cv2.findContours(dev_contours,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(sobel_8u,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
#cnt=contours[max_index]
cv2.drawContours(largest_contour, contours, max_index, (255,255,255), -1)
cv2.imshow('largest', largest_contour)
"""
for k in range(0,upper_bound):
    
    largest_contour = np.zeros(img.shape[:2],np.uint8)
    cv2.drawContours(largest_contour, contours, k, (255,255,255), 2)
    #cv2.imshow('largest', largest_contour)
    #cv2.imwrite('largest.jpg', mask)
"""


height, width = largest_contour.shape[:2]

all_white_pixels = []

#print height
#print width

for i in range(0,height):
    for j in range(0,width):
        if(largest_contour.item(i,j)==255):
            all_white_pixels.append([i,j])
            
#print all_white_pixels
matrix = np.array(all_white_pixels)

#row_mean = matrix.mean(axis=1) 
#col_mean = matrix.mean(axis=0) 

#print row_mean
#print col_mean

C = np.cov(matrix.T)
#print C

eigenvalues, eigenvectors = np.linalg.eig(C)

#print eigenvalues
#print eigenvectors

max_ev = max(eigenvalues)
max_index =  eigenvalues.argmax(axis=0)
#print type(eigenvalues)
#print max_ev
#print max_index

#print (eigenvectors[1,max_index]/eigenvectors[0,max_index])*(180/np.pi)
#print math.atan2((eigenvectors[1,max_index],eigenvectors[0,max_index]))*(180/np.pi)

y = eigenvectors[1,max_index]
x = eigenvectors[0,max_index]


angle = (np.arctan2(y,x))*(180/np.pi)

print angle
all_angles.append(angle)

k+=1
print 'Done'
print k

#M = cv2.getRotationMatrix2D((width/2,height/2),-angle/2,1)
print all_angles
M = cv2.getRotationMatrix2D((width/2,height/2),-(90+angle),1)
dst = cv2.warpAffine(img,M,(width,height))

print type(dst)

cv2.imshow('dst', dst)
dst = binarization.binary_img(dst)
cv2.imwrite('skewcorrected.jpg',dst)


cv2.waitKey(0)
cv2.destroyAllWindows()