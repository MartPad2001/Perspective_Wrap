import cv2
import numpy as np

img = cv2.imread("me/opencv/resources/pic4.jpg")
print(img.shape)

hor=np.hstack((img,img))
ver=np.vstack((img,img))

cv2.imshow("Image",hor)
cv2.imshow("Image2",ver)

cv2.waitKey(0)