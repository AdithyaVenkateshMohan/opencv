import sys
sys.path.append('C:\python64\Lib\site-packages')
import cv2
import numpy as np
import matplotlib.pyplot as plt

gokubg = cv2.imread(r'E:\opencv\gokubge.jpg')
mask = np.zeros(gokubg.shape[:2],np.uint8)
bg = np.zeros((1,65),np.float64)
fg = np.zeros((1,65),np.float64)

rec = (30, 30 , 900 , 900)

cv2.grabCut(gokubg,mask,rec,bg,fg,10, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask<1)|(mask==2),0,1).astype('uint8')
gokub = gokubg * mask2[:,:,np.newaxis]

gokubg=np.where(gokub > [0,0,0],gokubg,0)
print(gokub)
cv2.imshow('i think',gokubg)
plt.imshow(gokubg)
plt.colorbar()
plt.show()

