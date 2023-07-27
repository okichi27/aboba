import cv2
import numpy as np
image=cv2.imread("/home/rodion/yuliia0/aboba/test/4.jpg")
cv2.imshow("image",image)
crop = image[109:117, 132:139]
cv2.imshow("crop",crop)
cv2.imwrite("newnumer_2.1.jpg",crop)

cv2.waitKey()