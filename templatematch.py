import sys
sys.path.append('C:\python64\Lib\site-packages')
import numpy as np
import cv2

shawdow = cv2.imread('E:\opencv\clone.png')
shawdowgray = cv2.cvtColor(shawdow,cv2.COLOR_BGR2GRAY)
face =cv2.imread('E:\opencv\leaf.png')
facegray=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
cv2.imshow('face',face)
w , h = facegray.shape[::-1]
shadowrec =cv2.matchTemplate(shawdowgray,facegray,cv2.TM_CCOEFF_NORMED)
threshold =0.7
loc = np.where(shadowrec>threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(shawdow,pt,(pt[0]+w,pt[1]+h),(200,15,144),2)

cv2.imshow('detected',shawdow)
cv2.waitKey(0)
cv2.destroyAllWindows()

