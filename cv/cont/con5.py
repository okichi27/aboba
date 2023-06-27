import cv2
import numpy as np

img = cv2.imread("/home/rodion/yuliia0/aboba/cv/cont/cool.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray, (3,3))
cv2.imshow('cool', img)

canny= cv2.Canny(gray, 65, 65 * 2)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

mc = [None]*len(contours)
mu = [None]*len(contours)
for i in range(len(contours)):
    mu[i] = cv2.moments(contours[i])
    mc[i] = (mu[i]['m10'] / (mu[i]['m00'] + 1e-5), mu[i]['m01'] / (mu[i]['m00'] + 1e-5))

drawing = np.zeros((canny.shape[0], canny.shape[1], 3), dtype=np.uint8)

for i in range(len(contours)):
    cv2.drawContours(drawing, contours, i, (50,100,40), 2)
    cv2.circle(drawing, (int(mc[i][0]), int(mc[i][1])), 4, (50,100,40), -1)
    cv2.imshow('Contours', drawing)
cv2.waitKey(0)