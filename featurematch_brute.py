import sys
sys.path.append('C:\python64\Lib\site-packages')


import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('E:\opencv\clone.png',0)
img2 = cv2.imread(r'E:\opencv\wahf.png',0)
orb = cv2.ORB_create()

kv1,des1 = orb.detectAndCompute(img1,None)
kv2,des2 = orb.detectAndCompute(img2,None)


bf = cv2.BFMatcher(cv2.NORM_HAMMING , crossCheck = True)

matches = bf.match(des1,des2)
matches = sorted(matches , key = lambda x:x.distance)

img3 = cv2.drawMatches(img1,kv1,img2,kv2,matches[:10],None,flags=2)
plt.imshow(img3)
plt.show()

