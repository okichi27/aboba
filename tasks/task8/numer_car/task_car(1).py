import cv2
import pytesseract
import imutils
import re
import numpy as np

img = cv2.imread('/home/rodion/yuliia0/aboba/tasks/task8/numer_car/car_numer1.jpg')
img = imutils.resize(img, width=800 )
"""афінне перетворення"""

cv2.imshow('original', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray, (3,3))
gray = cv2.bilateralFilter(gray, 11, 17, 17)
'''gray = cv2.blur(gray, (3,3))'''

cv2.imshow('cool', img)

"""обрізка, квадрат"""
x1_numer=200
y1_numer=200
gray = gray[y1_numer:gray.shape[0]-y1_numer, x1_numer:gray.shape[1]-x1_numer]
'''gray = gray[y u:y d,x l:x r]'''
canny= cv2.Canny(gray, 190, 190 * 2)
cv2.imshow('non',canny )
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

boundRect = [None]*len(contours)
list=[]
for i, c in enumerate(contours):
    boundRect[i] = cv2.boundingRect(cv2.approxPolyDP(c, 3, True))
for i in range(len(contours)):
    x1=int(boundRect[i][0])
    x2=int(boundRect[i][0]+boundRect[i][2])
    y1=int(boundRect[i][1])
    y2=int(boundRect[i][1]+boundRect[i][3])
    '''if (boundRect[i][3])>12 and boundRect[i][2]>12:'''
    if 5*(boundRect[i][3])>boundRect[i][2] and 2*(boundRect[i][3])<boundRect[i][2]:
        lines=cv2.rectangle(gray, (x1+x1_numer+70, y1+y1_numer), (x2+x1_numer+70, y2+y1_numer), (100,10,40), 2)
        length=boundRect[i][2]
        """мікро-перерва для відшивання ліній"""
        list.append((x1,y1,x2,y2,length))
        """закінчення набору списку прямокутників-обітків"""
'''cv2.imshow('Rt', gray)'''
"""початок розслідування"""
sorted=sorted(list,key=lambda line:line[4],reverse=True)
'''print(sorted)'''
x1,y1,x2,y2,dov=sorted[0]
'''print(x1,y1,x2,y2,dov)'''
cv2.rectangle(img, (x1+x1_numer, y1+y1_numer), (x2+x1_numer,y2+y1_numer), (0,0,255), 2)
crop = img[y1+y1_numer:y2+y1_numer, x1+x1_numer:x2+x1_numer]
'''cv2.imshow("cropp",crop )'''
'''crop=cv2.GaussianBlur(crop,(3,3),0)'''

cv2.imshow("cropp",crop )

rows, cols, ch = crop.shape
pts1 = np.float32([[31, 12],
                   [34, 36],
                   [131, 6]])
 
pts2 = np.float32([[31, 12],
                   [31, 36],
                   [131, 12]])
 
M = cv2.getAffineTransform(pts1, pts2)
crop = cv2.warpAffine(crop, M, (cols, rows))

cv2.imshow("cropp af",crop )

crop_gray=cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

ker=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
crop_gray=cv2.filter2D(crop_gray,-1,ker)
'''cv2.imshow("crop_gray",crop_gray )'''
ret, thresh = cv2.threshold(crop_gray, 170, 255, cv2.THRESH_TOZERO)
'''cv2.imshow("Area",thresh )'''

text = pytesseract.image_to_string(thresh, config='stdout -c tessedit_char_whitelist=0123456789')
print ("text-",text,")")

only_number = re.findall(r'\d', text)
only_number = ' '.join(map(str, only_number))
print(only_number)

cv2.putText(img,only_number,(x1+x1_numer,y1+y1_numer-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)

width = int(img.shape[1] * 0.5)
height = int(img.shape[0] * 0.5)
img= cv2.resize(img, (width, height) )

cv2.imshow('Result', img)
cv2.waitKey(0)