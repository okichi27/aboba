import cv2
import numpy as np

img = cv2.imread("/home/rodion/yuliia0/aboba/cv/cont/cool.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray, (3,3))
cv2.imshow('cool', img)

canny= cv2.Canny(gray, 60, 60 * 2)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contours_poly = [None]*len(contours)
boundRect = [None]*len(contours)
centers = [None]*len(contours)
radius = [None]*len(contours)
for i, c in enumerate(contours):
    contours_poly[i] = cv2.approxPolyDP(c, 3, True)
    boundRect[i] = cv2.boundingRect(cv2.approxPolyDP(c, 3, True))
    centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])

drawing = np.zeros((canny.shape[0], canny.shape[1], 3), dtype=np.uint8)

for i in range(len(contours)):
    cv2.drawContours(drawing, contours_poly, i, (150,10,140))
    cv2.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), (int(boundRect[i][0]+boundRect[i][2]), 
    int(boundRect[i][1]+boundRect[i][3])), (100,10,40), 2)
    cv2.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), (50,10,140), 2)
    cv2.imshow('drawing', drawing)
cv2.waitKey(0)