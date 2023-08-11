import cv2
import pytesseract
import imutils
import re
import numpy as np 

img = cv2.imread('/home/rodion/yuliia0/aboba/tasks/task8/numer_car/car_numer1.jpg')


img = imutils.resize(img, width=800 )
gray_1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_1 = cv2.blur(gray_1, (3,3))
gray_1 = cv2.bilateralFilter(gray_1, 11, 17, 17)
'''gray = cv2.blur(gray, (3,3))'''

cv2.imshow('cool', img)

"""-----------------------------------------------------------------обрізка, квадрат"""
def crop_picture (x1_numer, y1_numer):
    gray = gray_1[y1_numer:gray_1.shape[0]-y1_numer, x1_numer:gray_1.shape[1]-x1_numer]
    return gray
gray=crop_picture (100, 100)
cv2.imshow(' gray', gray )
canny_param=170
x1_numer= y1_numer=100
def canny (canny_param):
    cv2.imshow('non gray',gray )
    canny= cv2.Canny(gray, canny_param, canny_param * 2)
    cv2.imshow('non',canny )
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    boundRect = [None]*len(contours)
    for i, c in enumerate(contours):
        boundRect[i] = cv2.boundingRect(cv2.approxPolyDP(c, 3, True))
    list=[]
    for i in range(len(contours)):
        x1=int(boundRect[i][0])
        x2=int(boundRect[i][0]+boundRect[i][2])
        y1=int(boundRect[i][1])
        y2=int(boundRect[i][1]+boundRect[i][3])
        '''if (boundRect[i][3])>12 and boundRect[i][2]>12:'''
        if 5*(boundRect[i][3])>boundRect[i][2] and 2*(boundRect[i][3])<boundRect[i][2]:
            cv2.rectangle(gray, (x1+x1_numer, y1+y1_numer), (x2+x1_numer, y2+y1_numer), (100,10,40), 2)
            list.append((x1,y1,x2,y2,boundRect[i][2]))
    '''cv2.imshow('Rt', gray)'''
    """----------------------------------------------------------------початок розслідування"""
    sorted_list=sorted(list,key=lambda line:line[4],reverse=True)
    '''print(sorted)'''
    x1,y1,x2,y2,dov=sorted_list[0]
    '''print(x1,y1,x2,y2,dov)'''
    cv2.rectangle(img, (x1+x1_numer, y1+y1_numer), (x2+x1_numer,y2+y1_numer), (100,255,40), 2)
    crop = img[y1+y1_numer:y2+y1_numer, x1+x1_numer:x2+x1_numer]
    cv2.imshow("cropp",crop )

    def text_picture (afina):

        crop_new=cv2.GaussianBlur(crop_new,(5,5),0)
        crop_gray=cv2.cvtColor(crop_new, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(crop_gray, 170, 255, cv2.THRESH_TRUNC)
        '''cv2.imshow("Area",thresh )'''

        text_img = pytesseract.image_to_string(thresh, config='stdout -c tessedit_char_whitelist=0123456789')
        print ("text-",text_img,")")
        return text_img
    
    text=text_picture(0)
    if len(text)<2:
        text=text_picture(1)
    number = re.findall(r'\d', text)
    number = ' '.join(map(str, number))
    print(number)

    cv2.putText(img,number,(x1+x1_numer,y1+y1_numer-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
    return img,number


picture,only_number=canny(170)
'''if len(only_number)<3:
    gray=crop_picture (200, 200)
    picture,only_number=canny(190)'''


cv2.imshow('Result',picture)
width = int(picture.shape[1] * 0.5)
height = int(picture.shape[0] * 0.5)
picture= cv2.resize(picture, (width, height) )

cv2.imshow('Result', picture)
cv2.waitKey(0)