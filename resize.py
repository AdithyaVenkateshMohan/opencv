import sys
sys.path.append('C:\python\Lib\site-packages')

import cv2
import numpy as pyn
from matplotlib import pyplot as plt

camcap= cv2.VideoCapture(0) # 0 because we are using first in-built web cam


while True:
    ret,frame = camcap.read() #reads the webcam data and stores it in frame and ret will know whether the web cam gets data or not
    graycam = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
    print(frame , "end")
    frame = cv2.resize(frame, (200, 200))
    cv2.imshow("video wah", frame)
    cv2.imshow("video kalla", graycam)
    if cv2.waitKey(1) & 0xFF== ord('q'): # will quit the window only when q is pressed
        break
camcap.release()
cv2.destroyAllWindows()
