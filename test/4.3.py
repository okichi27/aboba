import cv2
import numpy as np
import math

img=g=cv2.imread("/home/rodion/yuliia0/aboba/test/5.jpg")
'''cv2.imshow("original", img)'''

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
"""кінець кола"""

"""перевірка рамки"""
x=g.shape[0]
y=g.shape[1]
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

boundRect = [None]*len(contours)
for i, c in enumerate(contours):
    boundRect[i] = cv2.boundingRect(cv2.approxPolyDP(c, 3, True))
for i in range(len(contours)):
    cv2.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), (int(boundRect[i][0]+boundRect[i][2]), 
    int(boundRect[i][1]+boundRect[i][3])), (100,10,40), 2)
    crop = g[(int(boundRect[i][1])-rama):(int(boundRect[i][1]+boundRect[i][3]+rama)), (int(boundRect[i][0])-rama):(int(boundRect[i][0]+boundRect[i][2])+rama)]
    cv2.imshow("Area",crop )
"""кінець квадрат"""

'''gray_crop=cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
gray_crop = cv2.GaussianBlur(gray_crop, (5, 5),0)
image = cv2.Canny(gray_crop, 250, 350, 20)
cv2.imshow("i",image )
minLineLength=200
maxlineGap=20
lines=cv2.HoughLinesP(image,1,np.pi/180,30,minLineLength,maxlineGap)'''


def getcontours(crop,th1):
    contours, hierarchy= cv2.findContours(crop, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
         area= cv2.contourArea(contour)

         if area>1000:
             cv2.drawContours(th1, contours, -1, (0,255,0), 3)

             peri=cv2.arcLength(contour, True)

             approx=cv2.approxPolyDP(contour, 0.02*peri, True)
             cv2.imshow('xz', approx)
             objcor=len(approx)
             x, y, w, h = cv2.boundingRect(approx)

             if objcor ==7:

                 cv2.rectangle(th1,(x,y),(x+w,y+h), (255,0,0),2)
                 
                 startpoint= (approx[0][0][0],approx[0][0][1])
                 endpoint=(int((approx[3][0][0]+approx[4][0][0])/2),int((approx[3][0][1]+approx[4][0][1])/2))
                
                 slope=(startpoint[0]-endpoint[0])/(startpoint[1]-endpoint[1])
                 angle= math.degrees(math.atan(slope))
                 print(angle)
                 font= cv2.FONT_HERSHEY_SIMPLEX
                 cv2.putText(th1, 'angle= '+str(angle), (50,50), font, 1, (224,0,0), 2)
             else:
                 print ("lox")
                 pass
    

while True:
    blur=cv2.GaussianBlur(crop, (5,5), 0)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

    lower_red=np.array([0,100,100])
    upper_red=np.array([10,255,255])
    mask=cv2.inRange(hsv,lower_red, upper_red)

    result= cv2.bitwise_and(crop, crop, mask=mask)

    ab,th1=cv2.threshold(result, 130,255, cv2.THRESH_BINARY)
    th1=cv2.erode(th1,None, iterations=2)
    th1=cv2.dilate(th1, None, iterations=2)

    getcontours(mask,th1)
    
    cv2.imshow('th1', th1)
    cv2.imshow("frame", crop)
    cv2.waitKey(0)

'''crop_x=crop.shape[0]
crop_y=crop.shape[1]
print('crop x-',crop_x,'crop y- ',crop_y)
xcr=(crop_x/7)
ycr=(crop_y/9)*3
crop_x1=crop_x - xcr
crop_y1=crop_y - ycr
print('xcr-',xcr,'ycr- ',ycr)
print('crop_x1-',crop_x1,'crop_y1- ',crop_y1)
if lines is not None:
    for line in lines:
        x1,y1,x2,y2 = line[0]
        if xcr<x1<(crop_x1-20):
            if ycr<y1<crop_y1:
                dov=((y1-y2)**2+(x1-x2)**2)**0.5
                print("dov-", dov)
                cv2.line(crop,(x1,y1),(x2,y2),(0,255,0),2)  
            else:
                print("y none")  
        else:
            print("x none")
    cv2.imshow("show",crop)
else:
    print("biba")'''
