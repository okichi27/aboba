import cv2
import numpy as np
import glob

image=g=cv2.imread("/home/rodion/yuliia0/aboba/test/5.jpg")

"""початок знаходження кола"""
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rows = image.shape[0]
if rows >231:
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=32, minRadius=96, maxRadius=130)
else:
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=30, minRadius=75, maxRadius=85)

drawing = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8) 
for i in circles[0, :]:
  x=int(i[0])
  y=int(i[1])
  r=int(i[2])
  d=2*r
  cv2.circle(drawing, (x, y), r, (0, 0, 255), 2)
"""кінець кола"""

"""обрізка, квадрат"""
canny= cv2.Canny(drawing, 60, 60 * 2)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

boundRect = [None]*len(contours)
for i, c in enumerate(contours):
    boundRect[i] = cv2.boundingRect(cv2.approxPolyDP(c, 3, True))
for i in range(len(contours)):
    cv2.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), (int(boundRect[i][0]+boundRect[i][2]), 
    int(boundRect[i][1]+boundRect[i][3])), (100,10,40), 2)
    crop = g[(int(boundRect[i][1])):(int(boundRect[i][1]+boundRect[i][3])), (int(boundRect[i][0])):(int(boundRect[i][0]+boundRect[i][2]))]
    '''v2.imshow("Area",crop )'''
"""кінець квадрат"""
ker=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
img_display=cv2.GaussianBlur(crop,(3,3),0)
cv2.imshow("img_display",img_display )
img_display=cv2.filter2D(img_display,-1,ker)
cv2.imshow("img_display 2",img_display )

image = glob.glob('new*.jpg')
numer=0
for name in image:
    mask = cv2.imread(name)
    cv2.imshow("mask{}".format(numer),mask )
    numer+=1
    result=cv2.matchTemplate(crop,mask, cv2.TM_SQDIFF_NORMED)
    _minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(result, None)
    cv2.rectangle(crop, minLoc, (minLoc[0] + mask.shape[0], minLoc[1] + mask.shape[1]), (0,0,255), 2, 8, 0 )
    cv2.rectangle(crop, minLoc, (minLoc[0] + mask.shape[0], minLoc[1] + mask.shape[1]), (0,0,255), 2, 8, 0 )
    cv2.imshow('non', crop)


   















'''gray= cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
cv2.imshow("Area",gray )

def detect(thresh):
    percent_white_pix = 0
    digit = 0
    for d in digits:
        scaled_img = cv2.resize(thresh, d.shape[:2][::-1])
        bitwise = cv2.bitwise_and(d, cv2.bitwise_xor(scaled_img, d))
        before = np.sum(d == 255)
        matching = 100 - (np.sum(bitwise == 255) / before * 100)
        if percent_white_pix < matching:
            percent_white_pix = matching
            digit += 1
    return digit

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if cv2.contourArea(cnt) > 40:
        brect = cv2.boundingRect(cnt)
        x,y,w,h = brect
        roi = thresh[y:y+h, x:x+w]
        digit = detect(roi)
        cv2.rectangle(crop, brect, (0,0,240), 1)
        cv2.putText(crop, str(digit), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 240, 0), 2)
cv2.imshow('resultat',crop)'''
cv2.waitKey(0)
cv2.destroyAllWindows()