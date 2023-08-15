import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)

#draw circle
cv2.circle(img,(400,50),30,(255,255,0),3)

#text
cv2.putText(img," OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2)
cv2.imshow("Image",img)

cv2.waitKey(0)