# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:41:19 2015

@author: suryo
"""

import cv2
import numpy as np
import binarization

kernel = np.ones((5,5),np.uint8)

img = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/1.jpg',0)
original = img
img=cv2.medianBlur(img,5)
largest_contour = np.zeros(img.shape[:2],np.uint8)

sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

abs_sobel64f = np.absolute(sobely)
sobel_8u = np.uint8(abs_sobel64f)

#sobely = cv2.erode(sobely,kernel,iterations = 1)

cv2.imshow('sobely',sobel_8u)

new_sobel=cv2.medianBlur(sobel_8u,5)
cv2.imshow('sobel new',new_sobel)
new_sobel = 255 - new_sobel
yay = binarization.binary_img(new_sobel)
cv2.imshow('yay',yay)

contours, hierarchy = cv2.findContours(yay,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt=contours[max_index]


print max_index

cv2.drawContours(largest_contour, contours, max_index, (255,255,255), 2)
cv2.imshow('largest', largest_contour)
#cv2.imwrite('largest.jpg', mask)



height, width = largest_contour.shape[:2]

all_white_pixels = []

print height
print width

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
print C

eigenvalues, eigenvectors = np.linalg.eig(C)

print eigenvalues
print eigenvectors

max_ev = max(eigenvalues)
max_index =  eigenvalues.argmax(axis=0)
#print type(eigenvalues)
print max_ev
print max_index

print (eigenvectors[1,max_index]/eigenvectors[0,max_index])*(180/np.pi)
#print math.atan2((eigenvectors[1,max_index],eigenvectors[0,max_index]))*(180/np.pi)

y = eigenvectors[1,max_index]
x = eigenvectors[0,max_index]

"""
y = eigenvectors[max_index,1]
x = eigenvectors[max_index,0]
"""
angle = (np.arctan2(y,x))*(180/np.pi)

print angle

#M = cv2.getRotationMatrix2D((width/2,height/2),-angle/2,1)
M = cv2.getRotationMatrix2D((width/2,height/2),-(90+angle),1)
dst = cv2.warpAffine(original,M,(width,height))

print type(dst)

cv2.imshow('dst', dst)
dst = binarization.binary_img(dst)
cv2.imwrite('skewcorrected.jpg',dst)


cv2.waitKey(0)
cv2.destroyAllWindows()