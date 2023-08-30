
from numpy import argmax
from keras.utils import load_img
from keras.utils import img_to_array
from keras.models import load_model
import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import imutils


original = cv2.imread('/home/rodion/yuliia0/aboba/tasks/task8/numer bio1/lich1.jpg')
original = imutils.resize(original, width=800 )
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray, (3,3))
'''cv2.imshow('cool', original)'''

"""обрізка, квадрат"""
canny= cv2.Canny(gray, 240, 240 * 2)
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

"""початок розслідування"""
sorted=sorted(list,key=lambda line:line[4],reverse=True)
'''print(sorted)'''
x1,y1,x2,y2,dov=sorted[0]
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

canny_thresh = cv2.Canny(crop_gray, 300, 300 * 2)
canny_thresh = cv2.blur(canny_thresh, (3,3))
cv2.imshow('canny th', canny_thresh)

cont2, hier2 = cv2.findContours(canny_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
crop2=crop.copy()
contours_poly = [None]*len(cont2)
boundRect = [None]*len(cont2)
for i, c in enumerate(cont2):
    contours_poly[i] = cv2.approxPolyDP(c, 3, True)
    boundRect[i] = cv2.boundingRect(cv2.approxPolyDP(c, 3, True))
print("len(cont2)",len(cont2))
for i in range(len(cont2)):
    if boundRect[i][2]>2 and boundRect[i][3]>5:
        if boundRect[i][2]<30 and boundRect[i][3]<40:
            number_crop=crop2[int(boundRect[i][1]):int(boundRect[i][1]+boundRect[i][3]), int(boundRect[i][0]):int(boundRect[i][0]+boundRect[i][2])]
            '''cv2.imshow('drawing mi1', number_crop)'''
            number_crop=cv2.resize(number_crop, (28,28),)
            number_crop = cv2.resize(number_crop,(400, 400))
            number_crop = cv2.cvtColor(number_crop, cv2.COLOR_BGR2GRAY)
            '''cv2.imshow('original', number_crop)'''
            number_crop = cv2.equalizeHist(number_crop)
            kernel = np.ones((47, 47), np.uint8)
            kernel1 = np.ones((5, 5), np.uint8)
            number_crop=cv2.erode(number_crop, kernel)
            '''cv2.imshow('canny th 3',number_crop)'''
            n,dst = cv2.threshold(number_crop, 120, 255, cv2.THRESH_BINARY)
            dst = cv2.resize(number_crop,(28, 28))
            '''cv2.imshow('canny th dst', dst)'''
            n1,dst1 = cv2.threshold(dst, 115, 255, cv2.THRESH_BINARY)
            print('picture -', i)

            cv2.rectangle(crop, (int(boundRect[i][0]), int(boundRect[i][1])), (int(boundRect[i][0]+boundRect[i][2]), 
            int(boundRect[i][1]+boundRect[i][3])), (100,10,40), 2)

            cv2.imshow('drawing{}'.format(i), dst1)
            '''cv2.imshow('drawing crop', crop)'''
            cv2.imwrite('numer.task8.{}.jpg'.format(i), dst1)

            img = img_to_array(dst1)
            img = img.reshape(1, 28, 28, 1)
            img = img.astype('float32')
            img = img / 255.0
            
            model = load_model('/home/rodion/yuliia0/aboba/tasks/task8/network.task8/network2.2/final_model.h5')
            predict_value = model.predict(img)
            digit = argmax(predict_value)
            print(digit)
            cv2.putText(crop,str(digit),(int(boundRect[i][0]),  int(boundRect[i][1])-2),cv2.FONT_HERSHEY_SIMPLEX,0.4,(255,100,0),1)
            cv2.imshow('result', crop)

'''# evaluate the deep model on the test dataset
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
 
# load train and test dataset
def load_dataset():
 # load dataset
 (trainX, trainY), (testX, testY) = mnist.load_data()
 # reshape dataset to have a single channel
 trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
 testX = testX.reshape((testX.shape[0], 28, 28, 1))
 # one hot encode target values
 trainY = to_categorical(trainY)
 testY = to_categorical(testY)
 return trainX, trainY, testX, testY
 
# scale pixels
def prep_pixels(train, test):
 # convert from integers to floats
 train_norm = train.astype('float32')
 test_norm = test.astype('float32')
 # normalize to range 0-1
 train_norm = train_norm / 255.0
 test_norm = test_norm / 255.0
 # return normalized images
 return train_norm, test_norm
 
# run the test harness for evaluating a model
def run_test_harness():
 # load dataset
 trainX, trainY, testX, testY = load_dataset()
 # prepare pixel data
 trainX, testX = prep_pixels(trainX, testX)
 # load model
 model = load_model('final_model.h5')
 # evaluate model on test dataset
 _, acc = model.evaluate(testX, testY, verbose=0)
 print('> %.3f' % (acc * 100.0))
 
# entry point, run the test harness
run_test_harness()'''

cv2.waitKey(0)