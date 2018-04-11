import sys
sys.path.append('C:\python64\Lib\site-packages')

import cv2
import numpy as np

face_cas = cv2.CascadeClassifier('E:\opencv\haarcascadeface.xml')
eye_cas = cv2.CascadeClassifier('E:\opencv\haarcascade_eye.xml')

cam = cv2.VideoCapture(0)

while True:
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = face_cas.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),[255,0,0],2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]
        eye = eye_cas.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh)in eye:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),[0,0,255],1)
    cv2.imshow('rec',img)
    if cv2.waitKey(1) & 0xFF== ord('q'): # will quit the window only when q is pressed
        break

cam.release()
cv2.destroyAllWindows()
