import cv2
import numpy as np
import math
img=cv2.imread("/home/rodion/yuliia0/aboba/cv/trans/my.jpg")
cv2.imshow("original", img)
img = cv2.GaussianBlur(img, (3, 3),0)
img=g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 50, 200, 3)

lines = cv2.HoughLines(img, 1, np.pi / 180, 150, None)

for i in range(0, len(lines)):
 a = math.cos(lines[i][0][1])
 b = math.sin(lines[i][0][1])
 x0 = a * lines[i][0][0]
 y0 = b * lines[i][0][1]
 pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
 pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))

cv2.line (g, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
linesP = cv2.HoughLinesP(img, 1, np.pi / 180, 50, None, 50, 10)
for i in range(0, len(linesP)):
 l = linesP[i][0]
cv2.line (g, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
cv2.imshow("Standard Hough Line Transform", g)
cv2.imshow("Probabilistic Line Transform", g)

cv2.waitKey(0)