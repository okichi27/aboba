import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import imutils


img = cv2.imread('/home/rodion/yuliia0/aboba/tasks/task8/numer bio1/lich4.jpg')
img = imutils.resize(img, width=800 )
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray, (3,3))
'''cv2.imshow('cool', img)'''

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
'''cv2.imshow('Rt', gray)'''
"""початок розслідування"""
sorted=sorted(list,key=lambda line:line[4],reverse=True)
'''print(sorted)'''
x1,y1,x2,y2,dov=sorted[0]
'''print(x1,y1,x2,y2,dov)'''
cv2.rectangle(img, (x1, y1), (x2,y2), (100,255,40), 2)
crop=crop2 = img[y1:y2, x1:x2]
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

'''
crop_gray = imutils.resize(crop_gray, width=50 )
'''
canny_thresh = cv2.Canny(crop_gray, 360, 360 * 2)
canny_thresh = cv2.blur(canny_thresh, (3,3))
cv2.imshow('canny th', canny_thresh)

cont2, hier2 = cv2.findContours(canny_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
crop2=crop.copy()
contours_poly = [None]*len(cont2)
boundRect = [None]*len(cont2)
for i, c in enumerate(cont2):
    contours_poly[i] = cv2.approxPolyDP(c, 3, True)
    boundRect[i] = cv2.boundingRect(cv2.approxPolyDP(c, 3, True))
n=0
for i in range(len(cont2)):
    if boundRect[i][2]>8 and boundRect[i][3]>10:
        if boundRect[i][2]<30 and boundRect[i][3]<40:

            number_crop=crop2[int(boundRect[i][1]):int(boundRect[i][1]+boundRect[i][3]), int(boundRect[i][0]):int(boundRect[i][0]+boundRect[i][2])]
            cv2.imshow('drawing mi1', number_crop)
            number_crop=cv2.resize(number_crop, (28,28),)
            print('2-',number_crop.shape)

            cv2.rectangle(crop, (int(boundRect[i][0]), int(boundRect[i][1])), (int(boundRect[i][0]+boundRect[i][2]), 
            int(boundRect[i][1]+boundRect[i][3])), (100,10,40), 2)
            '''print("i new- ", i, "x-",boundRect[i][2], "y-",boundRect[i][3])'''
            n+=1
            mnist =tf.keras.datasets.mnist
            (x_train, y_train), (x_test, y_test)=mnist.load_data()

            '''model=tf.keras.models.load_model('/home/rodion/yuliia0/aboba/tasks/task8/network.task8/network_task8/handwritten.model')'''
            picture=np.invert(np.array([number_crop]))
            print(picture)

            prediction=model.predict(picture)
            print(f"ths digit is probably a {{{np.argmax(prediction)}}}")
            plt.imshow(picture[0],cmap=plt.cm.binary)
            plt.show()
            cv2.imshow('drawing{}'.format(i), number_crop)
            cv2.imshow('drawing mi', crop)
print('n-',n)
'''

text = pytesseract.image_to_string(thresh, config='stdout -c tessedit_char_whitelist=0123456789')
print ("text-",text)

only_number = re.findall(r'\d', text)
only_number = ' '.join(map(str, only_number))
print(only_number)

contours2,_=cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for contour in contours2:
    x,y,w,h=cv2.boundingRect(contour)
    if w>10 and h>10:
        cv2.putText(img,only_number,(x1, y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)
        break

img = imutils.resize(img, width=400 )'''

'''cv2.imshow('Result',thresh)'''
cv2.waitKey(0)
