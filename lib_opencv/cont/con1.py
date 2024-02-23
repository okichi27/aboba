import cv2
import numpy as np

img = cv2.imread("/home/rodion/yuliia0/aboba/cv/cont/cool.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray, (3,3))
cv2.imshow('cool', img)

canny= cv2.Canny(gray, 60, 60 * 2)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

drawing = np.zeros((canny.shape[0], canny.shape[1], 3), dtype=np.uint8)
for i in range(len(contours)):
    cv2.drawContours(drawing, contours, i, (250,50,190), 2, cv2.LINE_8, hierarchy, 0)
    cv2.imshow('Contours 1', drawing)

canny= cv2.Canny(gray, 20, 20 * 2)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

drawing = np.zeros((canny.shape[0], canny.shape[1], 3), dtype=np.uint8)
for i in range(len(contours)):
    cv2.drawContours(drawing, contours, i, (250,50,190), 2, cv2.LINE_8, hierarchy, 0)
    cv2.imshow('Contours 2', drawing)

canny= cv2.Canny(gray, 5, 5 * 2)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

drawing = np.zeros((canny.shape[0], canny.shape[1], 3), dtype=np.uint8)
for i in range(len(contours)):
    cv2.drawContours(drawing, contours, i, (250,50,190), 2, cv2.LINE_8, hierarchy, 0)
    cv2.imshow('Contours 3', drawing)

cv2.waitKey(0)