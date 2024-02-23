import cv2
import imutils
import numpy as np

original = cv2.imread('/home/rodion/yuliia0/aboba/tasks/task8/network.task8/network2.2/numer_net3.16.jpg')
cv2.imshow('1', original)
'''gray = cv2.blur(original, (3,3))'''
img = cv2.resize(original,(400, 400))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('original', gray)
gray = cv2.equalizeHist(gray)


kernel = np.ones((45, 45), np.uint8)
kernel1 = np.ones((5, 5), np.uint8)
gray=cv2.erode(gray, kernel)
cv2.imshow('canny th 3',gray)
n,dst = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
dst = cv2.resize(original,(28, 28))
cv2.imshow('canny th dst', dst)
n1,dst1 = cv2.threshold(dst, 128, 255, cv2.THRESH_BINARY)
dst1 = cv2.cvtColor(dst1, cv2.COLOR_BGR2GRAY)
cv2.imshow('canny th dst', dst1)

cv2.waitKey(0)