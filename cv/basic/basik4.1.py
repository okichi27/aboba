import cv2
import numpy as np
img= cv2.imread("/home/rodion/yuliia0/aboba/cv/basic/smoothing.jpg")
ker = np.ones((2, 2), np.uint8)
ero = cv2.erode(img, ker)
dil = cv2.dilate (img, ker)

ker = np.ones((10, 10), np.uint8)
ero2 = cv2.erode(img, ker)
dil2 = cv2.dilate (img, ker)

ker = np.ones((14, 3), np.uint8)
ero3 = cv2.erode(img, ker)
dil3 = cv2.dilate (img, ker)

cv2.imshow("original", img)
cv2.imshow("erode 2", ero)
cv2.imshow("dilate 2", dil)
cv2.imshow("erode 10", ero2)
cv2.imshow("dilate 10", dil2)
cv2.imshow("erode  rizne", ero3)
cv2.imshow("dilate rizne", dil3)
cv2.waitKey(0)