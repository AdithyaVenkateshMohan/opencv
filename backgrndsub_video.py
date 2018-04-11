import sys
sys.path.append('C:\python64\Lib\site-packages')
import cv2
import numpy as np

camcap= cv2.VideoCapture(0)
backgrndsub = cv2.createBackgroundSubtractorKNN()

while True:
    ret , frame = camcap.read()
    bgapp = backgrndsub.apply(frame)
    bgrev = cv2.bitwise_not(bgapp)
    res = cv2.bitwise_and(frame, frame, mask=bgrev)
    cv2.imshow('org',frame)
    cv2.imshow('fg',bgapp)
    cv2.imshow('invisbile',res)
    if cv2.waitKey(1) & 0xFF== ord('q'): # will quit the window only when q is pressed
        break



camcap.release()
cv2.destroyAllWindows()