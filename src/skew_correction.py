#python code to correct skew angle in images

#need to use concept of Eigen Vectors here

import cv2
import binarization
import numpy as np
kernel = np.ones((5,5),np.uint8)

img = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/Kandanu10.jpg',0)
cv2.imshow('original', img)
binary = binarization.binary_img(img)
cv2.imshow('binary', binary)
"""
dil = cv2.dilate(binary,kernel,iterations = 3)
cv2.imshow('dil', dil)
"""

height, width = img.shape[:2]

all_white_pixels = []

print height
print width

for i in range(0,height):
    for j in range(0,width):
        if(binary.item(i,j)==255):
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
angle = np.arctan2(y,x)*(180/np.pi)

M = cv2.getRotationMatrix2D((width/2,height/2),-angle,1)
dst = cv2.warpAffine(binary,M,(width,height))

print type(dst)

cv2.imshow('dst', dst)
cv2.imwrite('skewcorrected.jpg',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()