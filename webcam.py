import sys
sys.path.append('C:\python\Lib\site-packages')
import cv2
import numpy as npy
from matplotlib import pyplot as plt

camcap= cv2.VideoCapture(0) # 0 because we are using first in-built web cam
#savevi = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.mov',savevi,20.0,(640,480)) #to save the video


while True:
    ret,frame = camcap.read() #reads the webcam data and stores it in frame and ret will know whether the web cam gets data or not
    graycam = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
    print(frame , "end")
    cv2.imshow("video wah", frame)
    cv2.imshow("video kalla", graycam)
    if cv2.waitKey(1) & 0xFF== ord('q'): # will quit the window only when q is pressed
        break
camcap.release()
#out.release()
cv2.destroyAllWindows()

