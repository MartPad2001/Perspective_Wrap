import cv2
import numpy as np

img = cv2.imread("me/opencv/resources/lens.jpeg")
print(img.shape)

# resize image
imgResize=cv2.resize(img,(640,278))
print(imgResize.shape)

#crop image
imgCropped=imgResize[0:200,200:500]


# cv2.imshow("Real Image",img)
cv2.imshow("Resize Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)

cv2.waitKey(0)