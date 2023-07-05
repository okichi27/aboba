import cv2
import numpy as np
import math

img=g=cv2.imread("/home/rodion/yuliia0/aboba/test/1.jpg")
cv2.imshow("original", img)


"""початок знаходження кола"""
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rows = img.shape[0]
if rows >231:
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=32, minRadius=96, maxRadius=130)
else:
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=30, minRadius=75, maxRadius=85)


drawing = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8) 
for i in circles[0, :]:
  x=int(i[0])
  y=int(i[1])
  r=int(i[2])
  d=2*r
  cv2.circle(drawing, (x, y), r, (0, 0, 255), 2)
  cv2.imshow("orl", drawing)
"""кінець кола"""

"""перевірка рамки"""
x=g.shape[0]
y=g.shape[1]
print("x-",x,"y-",y)
ramax=x-d
ramay=y-d
if ramax and ramay >36:
   rama=15
else:
   rama=0
"""рамки є"""

"""обрізка, квадрат"""
canny= cv2.Canny(drawing, 60, 60 * 2)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

'''boundRect = [None]*len(contours)
for i, c in enumerate(contours):
    boundRect[i] = cv2.boundingRect(cv2.approxPolyDP(c, 3, True))
for i in range(len(contours)):
    cv2.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), (int(boundRect[i][0]+boundRect[i][2]), 
    int(boundRect[i][1]+boundRect[i][3])), (100,10,40), 2)
    crop = g[(int(boundRect[i][1])-rama):(int(boundRect[i][1]+boundRect[i][3]+rama)), (int(boundRect[i][0])-rama):(int(boundRect[i][0]+boundRect[i][2])+rama)]
    cv2.imshow("Area",crop )
"""кінець квадрат"""

cropnew = cv2.GaussianBlur(crop, (5, 5),0)
image = cv2.Canny(cropnew, 10, 200, 20)
lines = cv2.HoughLines(image, 1, np.pi / 180, 70, None)
print ("lines -",lines)

for i in range(0, len(lines)):
 a = math.cos(lines[i][0][1])
 b = math.sin(lines[i][0][1])
 x0 = a * lines[i][0][0]
 y0 = b * lines[i][0][1]
 pt1 = (int(x0 + 1*(-b)), int(y0 + 1*(a)))
 print("pt1=",pt1)
 pt2 = (int(x0 - 1*(-b)), int(y0 - 1*(a)))
 print("pt2=",pt2)

cv2.line (cropnew, pt1, pt2, (0,0,255), 6, cv2.LINE_AA)
linesP = cv2.HoughLinesP(image,rho = 1,theta = 1*np.pi/180,threshold = 60,minLineLength = 20,maxLineGap = 30)
for i in range(0, len(linesP)):
 l = linesP[i][0]
 cv2.line (crop, (l[0], l[1]), (l[2], l[3]), (0,200,100), 2, cv2.LINE_AA)
cv2.imshow("image",image )
cv2.imshow(" Line Transform", crop)'''

cv2.waitKey(0)