#python code to correct skew angle in images

#need to use concept of Eigen Vectors here

import cv2
import binarization

img = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/Kandanu10.jpg',0)
binary = binarization.binary_img(img)
cv2.imshow('binary', binary)

height, width = img.shape[:2]

matrix = []

print height
print width

for i in range(0,height):
    for j in range(0,width):
        if(binary.item(i,j)==255):
            matrix.append([i,j])
            
print matrix

cv2.waitKey(0)
cv2.destroyAllWindows()