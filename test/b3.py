import cv2
import numpy as np
img=g=cv2.imread("/home/rodion/yuliia0/aboba/test/3.jpg")
cv2.imshow("original", img)

"""початок знаходження кола"""
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rows = img.shape[0]
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, rows / 4, param1=100, param2=30, minRadius=90, maxRadius=130)

drawing = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8) 
for i in circles[0, :]:
  x=int(i[0])
  y=int(i[1])
  r=int(i[2])
  d=2*r
  cv2.circle(drawing, (x, y), r, (0, 0, 255), 2)
  
"""кінець кола"""
t=g.shape[0]
y=g.shape[1]
ramax=t-d
ramay=y-d
if ramax and ramay >33:
   rama=15
else:
   rama=0
canny= cv2.Canny(drawing, 60, 60 * 2)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

boundRect = [None]*len(contours)
for i, c in enumerate(contours):
    boundRect[i] = cv2.boundingRect(cv2.approxPolyDP(c, 3, True))
for i in range(len(contours)):
    cv2.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), (int(boundRect[i][0]+boundRect[i][2]), 
    int(boundRect[i][1]+boundRect[i][3])), (100,10,40), 2)
    print("1 -",int(boundRect[i][0]), "2 -",int(boundRect[i][1]), "3 -",int(boundRect[i][0]+boundRect[i][2]), "4 -",
    int(boundRect[i][1]+boundRect[i][3]))
    cv2.imshow("or", drawing)
    crop = g[(int(boundRect[i][1])-rama):(int(boundRect[i][1]+boundRect[i][3]+rama)), (int(boundRect[i][0])-rama):(int(boundRect[i][0]+boundRect[i][2])+rama)]
    cv2.imshow("Area",crop )
cv2.waitKey(0)