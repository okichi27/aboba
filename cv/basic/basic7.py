import cv2 
import numpy as np

img = cv2.imread ("/home/rodion/yuliia0/aboba/cv/basic/notyky.jpg")
cv2.imshow("orig",img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.bitwise_not(img)
bw =cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 15, -2)

hS = cv2.getStructuringElement(cv2.MORPH_RECT, (bw.shape[1] // 30, 1))
h = cv2.dilate(cv2.erode(bw, hS),hS)

vS = cv2.getStructuringElement(cv2.MORPH_RECT, (1, bw.shape[0] // 30))
v = cv2.dilate(cv2.erode(bw, vS),vS)
v = cv2.bitwise_not(v)
h = cv2.bitwise_not(h)

cv2.imshow("vertical", v)
cv2.imshow("horizontal", h)
cv2.waitKey (0)