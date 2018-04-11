import sys
sys.path.append('C:\python64\Lib\site-packages')
import numpy as np
from matplotlib import pyplot as plt
import cv2



imgna = cv2.imread('E:\opencv\watch.jpg',0)
#cv2.imshow('image',imgna)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

plt.imshow(imgna, cmap='gray', interpolation='bicubic')
plt.plot([12,100],[40,0],'r',linewidth=10)
plt.show()