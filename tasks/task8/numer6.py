import cv2
import numpy as np
SCALE = 3
THICK = 5
WHITE = (255, 255, 255)
digits = []
for digit in map(str, range(10)):
    (width, height), bline = cv2.getTextSize(digit, cv2.FONT_HERSHEY_SIMPLEX,
                                             SCALE, THICK)
    digits.append(np.zeros((height + bline, width), np.uint8))
    cv2.putText(digits[-1], digit, (0, height), cv2.FONT_HERSHEY_SIMPLEX,
                SCALE, WHITE, THICK)
    x0, y0, w, h = cv2.boundingRect(digits[-1])
    digits[-1] = digits[-1][y0:y0+h, x0:x0+w]
    cv2.imshow(digit, digits[-1])

color_test_image =g= cv2.imread('/home/rodion/yuliia0/aboba/test/5.jpg', cv2.IMREAD_COLOR)
"""початок знаходження кола"""
color_test_image = cv2.cvtColor(color_test_image, cv2.COLOR_BGR2GRAY)
rows = color_test_image.shape[0]
if rows >231:
    circles = cv2.HoughCircles(color_test_image, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=32, minRadius=96, maxRadius=130)
else:
    circles = cv2.HoughCircles(color_test_image, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=30, minRadius=75, maxRadius=85)

drawing = np.zeros((color_test_image.shape[0], color_test_image.shape[1], 3), dtype=np.uint8) 
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


gray_test_image = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
cv2.imshow('test_image', gray_test_image)
ret, thresh = cv2.threshold(gray_test_image, 180, 255, cv2.THRESH_BINARY_INV)

def detect(img):
    # сравниваем полученную цифру с нашей базой
    percent_white_pix = 0
    digit = -1
    for i, d in enumerate(digits):
        scaled_img = cv2.resize(img, d.shape[:2][::-1])
        # d AND (scaled_img XOR d)
        bitwise = cv2.bitwise_and(d, cv2.bitwise_xor(scaled_img, d))
        # результат определяется наибольшей потерей белых пикселей
        before = np.sum(d == 255)
        matching = 100 - (np.sum(bitwise == 255) / before * 100)
        #cv2.imshow('digit_%d' % (9-i), bitwise)
        if percent_white_pix < matching:
            percent_white_pix = matching
            digit = i
    return digit

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    # проверяется размер контура, чтобы избежать обработки "дефекта".
    if cv2.contourArea(cnt) > 30:
        # получаем прямоугольник, окружающий число
        brect = cv2.boundingRect(cnt)
        x,y,w,h = brect
        if w<23 and h<18:
            roi = thresh[y:y+h, x:x+w]
            # определение
            digit = detect(roi)
            cv2.rectangle(crop, brect, (0,255,0), 1)
            cv2.putText(crop, str(digit), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (190, 123, 0), 2)
cv2.imshow('resultat', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()