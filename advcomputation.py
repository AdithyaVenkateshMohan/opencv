import sys
sys.path.append('C:\python\Lib\site-packages')
import  cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('E:\opencv\gokuultra.png')
img2 = cv2.imread('E:\opencv\mainsvmimage.png')
logo = cv2.imread('E:\opencv\gokulogo.jpg')

#add = img1 + img2 # adds the two pics to one but has issues
#add=cv2.add(img1,img2) # add two pic pixels and matches with 0 to 255 scale
#add = cv2.addWeighted(img1,0.6,img2,0.3,0) #weighted summation on the pixels of the  image
rows,cols,channel = logo.shape
roi = img1[0:rows,0:cols]
gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(gray,190,255,cv2.THRESH_BINARY_INV)
invert = cv2.bitwise_not(mask)
bg = cv2.bitwise_and(roi,roi,mask=invert)
fg = cv2.bitwise_and(logo,logo,mask=mask)
wala = cv2.add(fg,bg)
img1[0:rows,0:cols] = wala
cv2.imshow('e',img1)
cv2.waitKey(0)
cv2.destroyAllWindows();