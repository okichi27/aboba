import cv2
import numpy as np

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

gray= cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Area",thresh )
digits = []
list=[0,1,2,3,4,5,6,7,8,9]
numer=0
'''цифри'''
while numer<len(list):
    digit=str(list[numer])
    numer+=1
    (width, height), bline = cv2.getTextSize(digit, cv2.FONT_HERSHEY_SIMPLEX,3, 5)
    digits.append(np.zeros((height, width), np.uint8))
    cv2.putText(digits[-1], digit, (0, height), cv2.FONT_HERSHEY_SIMPLEX,3, (255, 255, 255), 5)
    x0, y0, w, h = cv2.boundingRect(digits[-1])
    digits[-1] = digits[-1][y0:y0+h, x0:x0+w]
    '''cv2.imshow(digit, digits[-1])'''

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
cv2.imshow('resultat',crop)
cv2.waitKey(0)
cv2.destroyAllWindows()