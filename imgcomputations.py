import sys
sys.path.append('C:\python\Lib\site-packages')

import cv2
import numpy as pyn
from matplotlib import pyplot as plt

img = cv2.imread('E:\opencv\watch.jpg', cv2.IMREAD_COLOR)
#cv2.imshow('omg',img)
px = img[255,300]
img[300,400]=[255,0,0]
roi = img[37:111 ,107:194]
print(px)
img[0:74 ,0:87]=roi
img[100:300 ,200:600]=[255,0,200]
cv2.imshow('omg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()






