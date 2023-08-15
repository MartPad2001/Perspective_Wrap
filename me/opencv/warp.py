import cv2
import numpy as np

img = cv2.imread("me/opencv/resources/pic4.jpg")
print(img.shape)

width,height=250,350
pts1=np.float32([[145,351],[203,161],[557,412],[552,203]])#find points using paint app
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("warp",imgOutput)

cv2.waitKey(0)