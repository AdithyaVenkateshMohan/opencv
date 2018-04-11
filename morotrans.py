import sys
sys.path.append('C:\python\Lib\site-packages')
import numpy as np
import cv2

cam = cv2.VideoCapture(0)

while True:
    _,frame = cam.read()
    hsvframe=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #filtering range is specfied here

    lower_red = np.array([130,80,50])
    upper_red=np.array([180,200,180])


    #filtering op takes place here
    mask =cv2.inRange(hsvframe,lower_red,upper_red)
    res = cv2.bitwise_and(frame,frame,mask = mask)

    # blurring process is added to reduce the noise from the frame

    kernel = np.ones((5,5),np.uint8)
    erode= cv2.erode( res,kernel,iterations = 1)
    dialation = cv2.dilate(res, kernel, iterations=1)

    opening = cv2.morphologyEx(res,cv2.MORPH_OPEN ,kernel)
    closing = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('framwor',frame)
    cv2.imshow('erode', erode)
    cv2.imshow('dialate',dialation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)


    cv2.imshow('res',res)

    #checkout tophat and blackhat difference bet' openning and closing with the input of the image

    k=cv2.waitKey(1)& 0XFF == ord('q')
    if k==1:
        break

cv2.destroyAllWindows()
cam.release()


    #darkred =np.uint8([[[12,22,121]]])
    #darkredhsv =cv2.cvtColor(darkred,cv2.COLOR_BGR2HSV)