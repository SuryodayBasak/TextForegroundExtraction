# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:09:51 2015

@author: suryo
"""

import cv2
import numpy as np

kernel1 = np.ones((5,5),np.uint8)
kernel2 = np.ones((3,3),np.uint8)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

def binary_img(img):

    img_erode = cv2.dilate(img,kernel1,iterations = 2)
    blur=cv2.medianBlur(img,5)

    mask1 = np.ones(img.shape[:2],np.uint8)

    cl1 = clahe.apply(blur)

    circles_mask = cv2.dilate(cl1,kernel1,iterations = 1)
    circles_mask = (255-circles_mask)

    thresh = 1
    circles_mask = cv2.threshold(circles_mask, thresh, 255, cv2.THRESH_BINARY)[1]

    edges = cv2.Canny(cl1,100,200)

    edges = cv2.bitwise_and(edges,edges,mask=circles_mask) 

    dilation = cv2.dilate(edges,kernel1,iterations = 1)

    display = cv2.bitwise_and(img,img,mask=dilation) 

    cl2 = clahe.apply(display)
    cl2 = clahe.apply(cl2)

    ret,th = cv2.threshold(cl2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    th = 255 - th

    thg = cv2.adaptiveThreshold(display,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

    final = cv2.bitwise_and(dilation,dilation,mask=th) 

    finalg = cv2.bitwise_and(dilation,dilation,mask=thg) 

    finalg = 255 - finalg
    
    abso = cv2.bitwise_and(dilation,dilation,mask=finalg) 
    
    return abso
    
    
    
    
    
def skew_correction(img):
    largest_contour = np.zeros(img.shape[:2],np.uint8)

    binary = binary_img(img)
    contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt=contours[max_index]

    cv2.drawContours(largest_contour, contours, max_index, (255,255,255), 2)

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

    dst = binary_img(dst)
    
    return dst

def preprocess(img):
    return skew_correction(img)


cv2.waitKey(0)
cv2.destroyAllWindows()