import sys
sys.path.append('C:\python\Lib\site-packages')
import numpy as np
import cv2

cam = cv2.VideoCapture(0)

while True:
    _,frame = cam.read();
    hsvframe=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red = np.array([130,80,50])
    upper_red=np.array([180,200,180])

    mask =cv2.inRange(hsvframe,lower_red,upper_red)
    res = cv2.bitwise_and(frame,frame,mask = mask)

    # blurring process is added to reduce the noise from the frame

    kernel = np.ones((15,15),np.float32)/225
    smooth = cv2.filter2D(res,-1,kernel)

    blur=cv2.GaussianBlur(res,(5,5),0)
    medblur=cv2.medianBlur(res,5)

    cv2.imshow('framwor',frame)

    cv2.imshow('sm',smooth)
    cv2.imshow('blur', blur)
    cv2.imshow('medblur', medblur)

    cv2.imshow('res',res)

    k=cv2.waitKey(1)& 0XFF == ord('q')
    if k==1:
        break

cv2.destroyAllWindows()
cam.release()


    #darkred =np.uint8([[[12,22,121]]])
    #darkredhsv =cv2.cvtColor(darkred,cv2.COLOR_BGR2HSV)