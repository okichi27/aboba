import cv2
import numpy as np

img = cv2.imread("/home/rodion/yuliia0/aboba/cv/histo/cat2.png")
cv2.imshow("original", img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hue = np.empty(img.shape, img.dtype)
cv2.mixChannels([img], [hue], (0, 0))

hist = cv2.calcHist([hue], [0], None, [max(50, 2)], [0, 180], accumulate=False)
cv2.normalize(hist, hist, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

b= cv2.calcBackProject([hue], [0], hist, [0, 180], scale=1)

cv2.imshow('histo', b)
cv2.waitKey(0)