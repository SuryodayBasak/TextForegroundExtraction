# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:03:59 2015

@author: suryo
"""

import cv2
import prep
kernel = np.ones((5,5),np.uint8)

img = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/1.jpg',0)
largest_contour = np.zeros(img.shape[:2],np.uint8)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

sobely = cv2.erode(sobely,kernel,iterations = 1)
sobely = cv2.dilate(sobely,kernel,iterations = 1)

cv2.imshow('sobely', sobely)


contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    #contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #areas = [cv2.contourArea(c) for c in contours]
total_area=0
area_count=0
    
for c in contours:
    areas = cv2.contourArea(c) 
    total_area = total_area + cv2.contourArea(c)
    area_count+=1
        
areas = [cv2.contourArea(c) for c in contours]
print total_area
mean_area = total_area/area_count
print mean_area
max_index = np.argmax(areas)
print 'Max area = '
print areas[max_index]
cnt=contours[max_index]

    
cv2.drawContours(largest_contour, contours, max_index, (255,255,255), 2)
    
cv2.imshow("Largest",largest_contour)

height, width = largest_contour.shape[:2]

all_white_pixels = []

for i in range(0,height):
    for j in range(0,width):        
        if(largest_contour.item(i,j)==255):
            all_white_pixels.append([i,j])
            

matrix = np.array(all_white_pixels)
    
C = np.cov(matrix.T)

eigenvalues, eigenvectors = np.linalg.eig(C)

max_ev = max(eigenvalues)

max_index =  eigenvalues.argmax(axis=0)

y = eigenvectors[1,max_index]
x = eigenvectors[0,max_index]

angle = (np.arctan2(y,x))*(180/np.pi)

M = cv2.getRotationMatrix2D((width/2,height/2),-(90+angle),1)
dst = cv2.warpAffine(img,M,(width,height))

dst = prep.binary_img(dst)

cv2.waitKey(0)
cv2.destroyAllWindows()