import cv2
import numpy as np
import math

img=g=cv2.imread("/home/rodion/yuliia0/aboba/test/2.jpg")
cv2.imshow("original", img)
cv2.waitKey(0)
skl1=int(input("Введіть максимальне значення верхньої поділки: "))
skl2=int(input("Введіть максимальне значення нижньої поділки: "))

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
    """cv2.imshow("Area",crop )"""
"""кінець квадрат"""

"""початок пошуку стрілки"""
gray_crop=cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
gray_crop = cv2.GaussianBlur(gray_crop, (5, 5),0)
dst = cv2.Laplacian (gray_crop, cv2.CV_8U, ksize=1)
image = cv2.Canny(dst, 70, 150, 70)
cv2.imshow("canny",image )
minLineLength=200
maxlineGap=10
lines=cv2.HoughLinesP(image,1,np.pi/180,30,minLineLength,maxlineGap)

crop_x=crop.shape[0]
crop_y=crop.shape[1]
xcr=(crop_x/6)
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
                cv2.line(crop,(x1,y1),(x2,y2),(0,255,0),2)
            else:
                print("y none")  
else:
    print("biba")
"""закінчення пошуку стрілки"""
"""початок розслідування"""
print(list)
sorted=sorted(list,key=lambda line:line[4],reverse=True)
print(sorted)
d=0
u=0
n=0
if len(list)>2:
    k=3
else:
    k=2

while n<k:
    x1,y1,x2,y2,dov=list[n]
    n=n+1
    print("shoce - ",(crop.shape[1])/2)
    """почали шукати кут"""
    if 0<y1<((crop.shape[1])*0.5):
        while u<1:
            u=u+1
            print("u",u)
            print("--------верх:")
            kat=((y1-y2)**2)**0.5
            print("katet-", kat)
            print("dov-", dov)
            sin=kat/dov
            print("sin-", sin)
            if 0<x1<(crop.shape[0]*0.5):
                kut=np.arcsin(sin)
                print("kut gr-", kut)
                up=(skl1/(np.pi))*kut
                l_up=str(round(up,2))
                crop=cv2.putText(crop,l_up,(8,15),cv2.FONT_HERSHEY_SIMPLEX,0.4,(250,2,0),1,cv2.LINE_AA)
                print("ліво верх")
                cv2.line(crop,(x1,y1),(x2,y2),(0,255,0),2)
            else:
                kut=(np.pi)-np.arcsin(sin)
                print("kut gr-", kut)
                up=(skl1/(np.pi))*kut
                r_up=str(round(up,2))
                crop=cv2.putText(crop,r_up,(8,15),cv2.FONT_HERSHEY_SIMPLEX,0.4,(250,2,0),1,cv2.LINE_AA)
                print("право верх")
                cv2.line(crop,(x1,y1),(x2,y2),(0,255,0),2)
        else:
            print("None up line")
    else:
        if d<1:
            d+=1
            print("d",d)
            print("--------низ:")
            print("y1-",y1,"y2-",y2)
            kat=((y1-y2)**2)**0.5
            print("katet-", kat)
            print("dov-", dov)
            sin=kat/dov
            print("sin-", sin)
            if 0<x1<(crop.shape[0]*0.5):
                kut=np.arcsin(sin)
                print("kut gr-", kut)
                down=(skl2/(np.pi))*kut
                rad=57.2958*kut
                print("rad", rad)
                l_down=str(round(down,2))
                crop=cv2.putText(crop,l_down,(crop.shape[0]-45,crop.shape[1]-8),cv2.FONT_HERSHEY_SIMPLEX,0.4,(250,2,0),1,cv2.LINE_AA)
                print("ліво низ")
                cv2.line(crop,(x1,y1),(x2,y2),(0,255,0),2)
            else:
                kut=(np.pi)-np.arcsin(sin)
                print("kut gr-", kut)
                down=(skl2/(np.pi))*kut
                r_down=str(round(down,2))
                crop=cv2.putText(crop,r_down,(crop.shape[0]-45,crop.shape[1]-8),cv2.FONT_HERSHEY_SIMPLEX,0.4,(250,2,0),1,cv2.LINE_AA)
                print("право низ")
                cv2.line(crop,(x1,y1),(x2,y2),(0,255,0),2)
        else:
            print("None down line")
    """шукаємо """
    cv2.imshow("show",crop)
else:
    print("oj")
cv2.waitKey(0)