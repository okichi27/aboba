import cv2
import numpy as np
img= cv2.imread("/home/rodion/yuliia0/aboba/cv/basic/cat.jpg")
ker = np.ones((5, 5), np.uint8)
open = cv2.dilate(cv2.erode(img, ker),ker)
close = cv2.erode(cv2.dilate(img, ker),ker)
morph=cv2.dilate (img, ker)-cv2.erode(img, ker)
top=img-open
bl=close-img

cv2.imshow("original", img)
cv2.imshow("open", open)
cv2.imshow("close", close)
cv2.imshow("morphological gradient", morph)
cv2.imshow("Top Hat", top)
cv2.imshow("Black Hat", bl)
cv2.waitKey(0)