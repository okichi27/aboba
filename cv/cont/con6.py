import cv2
import numpy as np

img = np.zeros((700, 700), dtype=np.uint8)

vert = [None]*8
vert[0] = (350, 220)
vert[1] = (220, 120)
vert[2] = (90, 180)
vert[3] = (120, 330)
vert[4] = (350, 580)
vert[5] = (600, 330)
vert[6] = (620, 180)
vert[7] = (500, 130)

for i in range(8):
    cv2.line(img, vert[i],  vert[(i+1)%8], ( 255 ), 3)

contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

raw = np.empty(img.shape, dtype=np.float32)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        raw[i,j] = cv2.pointPolygonTest(contours[0], (j,i), True)

minVal, maxVal, _, maxDistPt = cv2.minMaxLoc(raw)
minVal = abs(minVal)
maxVal = abs(maxVal)

drawing = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if raw[i,j] < 0:
            drawing[i,j,0] = 255 - abs(raw[i,j]) * 255 / minVal
        elif raw[i,j] > 0:
            drawing[i,j,2] = 255 - raw[i,j] * 255 / maxVal
        else:
            drawing[i,j,0] = 255
            drawing[i,j,1] = 255
            drawing[i,j,2] = 255

cv2.circle(drawing,maxDistPt, int(maxVal),(255,0,255), 1, cv2.LINE_8, 0)

cv2.imshow('omg', img)
cv2.imshow('cool drawing', drawing)
cv2.waitKey(0)