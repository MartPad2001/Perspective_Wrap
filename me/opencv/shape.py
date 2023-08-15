import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)

#print red color
img[:]=0,0,255
print(img)


#draw line from (512,0) to (0,512)
cv2.line(img,(512,0),(0,512),(0,255,0),3)

#draw line from (0,0) to (512,512)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),3)

# draw rectangle
cv2.rectangle(img,(0,0),(250,350),(0,0,0),2)

# draw rectangle with fill
cv2.rectangle(img,(512,0),(250,350),(0,0,0),cv2.FILLED)
cv2.imshow("Image",img)



cv2.waitKey(0)