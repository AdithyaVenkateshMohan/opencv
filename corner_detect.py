import sys
sys.path.append('C:\python64\Lib\site-packages')
import cv2
import numpy as np

img = cv2.imread(r'E:\opencv\gokucon.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corner= cv2.goodFeaturesToTrack(gray , 200 , 0.3 , 35 )

for corners in corner:
    x,y = corners.ravel()
    cv2.circle(img,(x,y),3,[255,34,100],-1)

cv2.imshow('cor',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

