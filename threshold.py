#thresholding is used to simplyfy the image basic thresholding is kind of 0 or 1
#extreme simplify like gray sacle conver but this more than that

import sys
sys.path.append('C:\python\Lib\site-packages')
import numpy as np
import cv2

book = cv2.imread('E:\opencv\gokuultra.png')
graybook = cv2.cvtColor(book,cv2.COLOR_BGR2GRAY)
retval,thresbook = cv2.threshold(book,12,255,cv2.THRESH_BINARY) #normal thresholding methods if the image is in low light low pixel value as high if high light expose high as low
retval2,thresgray=cv2.threshold(graybook,12,255,cv2.THRESH_BINARY) # thres on gray scale
gausbook = cv2.adaptiveThreshold(graybook,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1) # adaptive threshold
retval2,thresotsu =cv2.threshold(graybook,12,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # otsu charc added
cv2.imshow('original',book)
cv2.imshow('threshold',thresbook)
cv2.imshow('thresgray',thresgray)
cv2.imshow('thresgaus',gausbook)
cv2.imshow('thresotsu',thresotsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
