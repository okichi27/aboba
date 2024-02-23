import cv2
import numpy as np

img = cv2.imread("/home/rodion/yuliia0/aboba/cv/cont/cool.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray, (3,3))
cv2.imshow('cool', img)

canny= cv2.Canny(gray, 65, 65 * 2)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

minRect = [None]*len(contours)
minEllipse = [None]*len(contours)
for i, c in enumerate(contours):
    minRect[i] = cv2.minAreaRect(c)
    if c.shape[0] > 5:
        minEllipse[i] = cv2.fitEllipse(c)

drawing = np.zeros((canny.shape[0], canny.shape[1], 3), dtype=np.uint8)
for i, c in enumerate(contours):
    cv2.drawContours(drawing, contours, i, (150,10,140))
    cv2.ellipse(drawing, minEllipse[i], (50,100,40), 2)
    box = cv2.boxPoints(minRect[i])
    box = np.intp(box)
    cv2.drawContours(drawing, [box], 0, (10,10,140))
    cv2.imshow('Contours', drawing)
cv2.waitKey(0)