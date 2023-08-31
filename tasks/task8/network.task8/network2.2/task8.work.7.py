
from numpy import argmax
from keras.utils import load_img
from keras.utils import img_to_array
from keras.models import load_model
import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import imutils


original = cv2.imread('/home/rodion/yuliia0/aboba/tasks/task8/numer bio1/lich7.jpg')
original = imutils.resize(original, width=800 )
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray, (3,3))
'''cv2.imshow('cool', img)'''

"""обрізка, квадрат"""
canny= cv2.Canny(gray, 230, 230 * 2)
cv2.imshow('non',canny )
cont1, hier1 = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

boundRect = [None]*len(cont1)
list=[]
for i, c in enumerate(cont1):
    boundRect[i] = cv2.boundingRect(cv2.approxPolyDP(c, 3, True))
for i in range(len(cont1)):
    x1=int(boundRect[i][0])
    x2=int(boundRect[i][0]+boundRect[i][2])
    y1=int(boundRect[i][1])
    y2=int(boundRect[i][1]+boundRect[i][3])
    '''if (boundRect[i][3])>12 and boundRect[i][2]>12:'''
    lines=cv2.rectangle(gray, (x1, y1), (x2, y2), (100,10,40), 2)
    length=boundRect[i][2]
    """мікро-перерва для відшивання ліній"""
    list.append((x1,y1,x2,y2,length))
    """закінчення набору списку прямокутників-обітків"""
#print('list',list)
"""початок розслідування"""
sorted_=sorted(list,key=lambda line:line[4],reverse=True)
#print('sort',sorted)
x1,y1,x2,y2,dov=sorted_[0]
'''print(x1,y1,x2,y2,dov)'''
cv2.rectangle(original, (x1, y1), (x2,y2), (100,255,40), 2)
crop=crop2 = original[y1:y2, x1:x2]
'''crop=cv2.GaussianBlur(crop,(3,3),0)'''
crop_gray=cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
'''ret, thresh = cv2.threshold(crop_gray, 110, 255, cv2.THRESH_TRUNC)'''
'''thresh = imutils.resize(crop_gray, width=200 )
crop_gray = cv2.bilateralFilter(crop_gray, 11, 17, 17)'''
crop_gray = cv2.bilateralFilter(crop_gray, 11, 17, 17)
'''thresh = imutils.resize(crop_gray, width=200 )'''
'''ret, thresh = cv2.threshold(crop_gray, 80, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Area",thresh )
'''

canny_thresh = cv2.Canny(crop_gray, 260, 260 * 2)
canny_thresh = cv2.blur(canny_thresh, (3,3))
cv2.imshow('canny th', canny_thresh)
cont2, hier2 = cv2.findContours(canny_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
crop2=crop.copy()
contours_poly = [None]*len(cont2)
boundRect = [None]*len(cont2)
for i, c in enumerate(cont2):
    contours_poly[i] = cv2.approxPolyDP(c, 3, True)
    boundRect[i] = cv2.boundingRect(cv2.approxPolyDP(c, 3, True))


list_numer=[]
for i in range(len(cont2)):
    if boundRect[i][2]>4 and boundRect[i][3]>6:
        if boundRect[i][2]<30 and boundRect[i][3]<40:

            length_numer=boundRect[i][2]+boundRect[i][3]

            x1=int(boundRect[i][0])
            x2=int(boundRect[i][0]+boundRect[i][2])
            y1=int(boundRect[i][1])
            y2=int(boundRect[i][1]+boundRect[i][3])
            print(i, "----",x1,x2,y1,y2)

            list_numer.append((x1,y1,x2,y2,length_numer))

print('list_numer ---',list_numer)
print(len(list_numer))

sorted_numer=sorted(list_numer, key=lambda line:line[4], reverse=True)
print("1 sorted_numer ---- ",sorted_numer)

print('1 len---',len(sorted_numer))
n=0
last_list=[]
while n<len(sorted_numer):
    x1,y1,x2,y2,length_numer=sorted_numer[n]
    k=n+1
    print("bibka--",n)
    while k<len(sorted_numer):
        x_1,y_1,x_2,y_2,length_numer2=sorted_numer[k]
        if y1+10>y_1 and y1-10<y_1:
            print("biba--",k)
            if x1<x_1 and x2>x_1:
                sorted_numer.pop(k)
                print(x1,'<',x2)
                print()      

        else:
            sorted_numer.pop(k)
        k+=1
    n+=1


print("2 sorted_numer ---- ",sorted_numer)
print('2 len---',len(sorted_numer))

crop2=crop.copy()

ramka_numer=0
while ramka_numer<len(sorted_numer):
    x1,y1,x2,y2,length_numer=sorted_numer[ramka_numer]
    cv2.rectangle(crop, (x1, y1), (x2, y2), (100,10,40), 2)

    number_crop=crop2[y1:y2,x1:x2]
    number_crop=cv2.resize(number_crop, (28,28),)
    number_crop = cv2.resize(number_crop,(400, 400))
    number_crop = cv2.cvtColor(number_crop, cv2.COLOR_BGR2GRAY)
    cv2.imshow('original', number_crop)
    number_crop = cv2.equalizeHist(number_crop)
    kernel = np.ones((47, 47), np.uint8)
    number_crop=cv2.erode(number_crop, kernel)
    cv2.imshow('canny th 3',number_crop)
    n,dst = cv2.threshold(number_crop, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow('canny th dst', dst)
    dst=cv2.resize(dst, (28,28),)
    n1,dst1 = cv2.threshold(dst, 115, 255, cv2.THRESH_BINARY)
    print('picture -', ramka_numer)

    cv2.imshow('drawing{}'.format(ramka_numer), dst1)
    ramka_numer+=1
    img = img_to_array(dst1)
    img = img.reshape(1, 28, 28, 1)
    img = img.astype('float32')
    img = img / 255.0
                    
    model = load_model('/home/rodion/yuliia0/aboba/tasks/task8/network.task8/network2.2/final_model.h5')
    predict_value = model.predict(img)
    digit = argmax(predict_value)
    print(digit)
    cv2.putText(crop,str(digit),(x1,  y1-2),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,100,0),2)
    cv2.imshow('result', crop)
cv2.waitKey(0)