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

"""початок пошуку стрілки"""
gray_crop=cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
gray_crop = cv2.GaussianBlur(gray_crop, (5, 5),0)
image = cv2.Canny(gray_crop, 250, 350, 20)
cv2.imshow("i",image )
minLineLength=200
maxlineGap=20
lines=cv2.HoughLinesP(image,1,np.pi/180,30,minLineLength,maxlineGap)

crop_x=crop.shape[0]
crop_y=crop.shape[1]
xcr=(crop_x/7)
ycr=(crop_y/9)*3
crop_x1=crop_x - xcr
crop_y1=crop_y - ycr

list=[]

if lines is not None:
    for line in lines:
        x1,y1,x2,y2 = line[0]
        print("  x1-",x1,"  y1-",y1,"  x2-",x2,"  y2-",y2)
        if xcr<x1<(crop_x1-20):
            if ycr<y1<crop_y1:
                """шукаємо кут"""
                dov=((y1-y2)**2+(x1-x2)**2)**0.5
                print("dov-", dov)
                """мікро-перерва для відшивання ліній"""
                list.append((x1,y1,x2,y2,dov))
            else:
                print("y none")  
else:
    print("biba")
"""закінчення пошуку стрілки"""
"""початок розслідування"""
print(list)
sorted=sorted(list,key=lambda line:line[4],reverse=True)
print(sorted)

n=0
while n<2:
    x1,y1,x2,y2,dov=list[n]
    n=n+1
    kat=((x1-x2)**2)**0.5
    print("kat-", kat)
    sin=kat/dov
    print("sin-", sin)
    kut=np.arcsin(sin)
    print("kut gr-", kut)
    """закінчили кут"""
    vysota=crop.shape[1]-2
    print('vysota',int(vysota*0.5-1), "po ",vysota)
    if (vysota*0.5-1)<y2<vysota:
        if (crop.shape[0]*0.5)<x1<crop.shape[0]:
            print("ліво верх")
            print("tak",y2)
            up=(10/180)*kut
            up=str(round(up,2))
            crop=cv2.putText(crop,up,(8,15),cv2.FONT_HERSHEY_SIMPLEX,0.4,(250,2,0),1,cv2.LINE_AA)
            print("up",up)
        else:
            print("право верх")
    else:
        print("ni",y2)
        if (crop.shape[0]*0.5)<x1<crop.shape[0]:
            print("ліво низ")
            down=(120/180)*kut
            down=str(round(down,2))
            crop=cv2.putText(crop,down,(crop.shape[0]-35,crop.shape[1]-8),cv2.FONT_HERSHEY_SIMPLEX,0.4,(250,2,0),1,cv2.LINE_AA)
            print("down",down)
        else:
            print("право низ")
    """шукаємо від 180 на шкалу скільки має бути кут та виводимо текстком зверху зліва та знизу зправа"""
    cv2.line(crop,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.imshow("show",crop)
else:
    print("oj")
cv2.waitKey(0)