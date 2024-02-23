import cv2 
import numpy as np

img = cv2.imread("/home/rodion/yuliia0/aboba/cv/histo/cat2.png")

bgr= cv2.split(img)

b = cv2.calcHist(bgr, [0], None, [256], (0, 256), accumulate=False)
g = cv2.calcHist(bgr, [1], None, [256], (0, 256), accumulate=False)
r = cv2.calcHist(bgr, [2], None, [256], (0, 256), accumulate=False)

cv2.normalize(b, b, alpha=0, beta=400, norm_type=cv2.NORM_MINMAX)
cv2.normalize(g, g, alpha=0, beta=400, norm_type=cv2.NORM_MINMAX)
cv2.normalize(r, r, alpha=0, beta=400, norm_type=cv2.NORM_MINMAX)

hist = np.zeros((400, 512, 3), dtype=np.uint8)

for i in range(1, 256):
    cv2.line(hist, ( 2*(i-1), 400 - int(b[i-1]) ), ( 2*(i), 400 - int(b[i]) ), ( 255, 0, 0), thickness=2)
    cv2.line(hist, ( 2*(i-1), 400 - int(g[i-1]) ), ( 2*(i), 400 - int(g[i]) ), ( 0, 255, 0), thickness=2)
    cv2.line(hist, ( 2*(i-1), 400 - int(r[i-1]) ), ( 2*(i), 400 - int(r[i]) ), ( 0, 0, 255), thickness=2)

cv2.imshow('original', img)
cv2.imshow('Hist', hist)
cv2.waitKey(0)