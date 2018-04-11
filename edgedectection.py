import sys
sys.path.append('C:\python\Lib\site-packages')
import numpy as np
import cv2

cam = cv2.VideoCapture(0)

while True:
    _,frame = cam.read()
    #frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(frame,cv2.CV_64F)
    sobelx= cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edge = cv2.Canny(frame,160,170)
# higher values less edge v.usefull
    cv2.imshow('framwor',frame)
    cv2.imshow('lap', lap)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('edge', edge)

    k=cv2.waitKey(1)& 0XFF == ord('q')
    if k==1:
        break

cv2.destroyAllWindows()
cam.release()


