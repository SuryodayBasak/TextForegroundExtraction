#python code to correct skew angle in images

#need to use concept of Eigen Vectors here

import cv2
import binarization
import numpy as np

img = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/Kandanu10.jpg',0)
binary = binarization.binary_img(img)
cv2.imshow('binary', binary)

height, width = img.shape[:2]

all_white_pixels = []

print height
print width

for i in range(0,height):
    for j in range(0,width):
        if(binary.item(i,j)==255):
            all_white_pixels.append([i,j])
            
print all_white_pixels
matrix = np.array(all_white_pixels)

row_mean = matrix.mean(axis=1) 
col_mean = matrix.mean(axis=0) 

print row_mean
print col_mean

cv2.waitKey(0)
cv2.destroyAllWindows()