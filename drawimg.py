import sys
sys.path.append('C:\python\Lib\site-packages') # to import the lib
import cv2
import numpy as np
from matplotlib import pyplot as pl

img= cv2.imread('E:\opencv\watch.jpg',1)
cv2.line(img,(20,20),(100,100),(255,255,0),10)
cv2.rectangle(img,(10,10),(200,200),(255,0,255),20)
cv2.circle(img,(200,200),100,(34,45,78),10)
points = np.array([[100,20],[200,300],[40,50],[30,300]],np.int32) #ploygon pts in the image
cv2.polylines(img,[points],True,(56,155,200),5)

font = cv2.FONT_HERSHEY_SIMPLEX;
cv2.putText(img,'nee yen ethayam',(255,400),font,1,(200,120,180),1,cv2.LINE_AA) #put the string in the image
cv2.imshow('vallla',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


