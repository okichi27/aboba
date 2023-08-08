import cv2
import pytesseract
import re

img = cv2.imread('/home/rodion/yuliia0/aboba/tasks/task8/numer bio1/lich3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray, (3,3))
cv2.imshow('cool', img)

"""обрізка, квадрат"""
'''gray = gray[110:gray.shape[1]-110, 80:gray.shape[0]-80]'''
canny= cv2.Canny(gray, 240, 240 * 2)
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
    if 100*(boundRect[i][3])>boundRect[i][2] and 0*(boundRect[i][3])<boundRect[i][2]:
        lines=cv2.rectangle(gray, (x1, y1), (x2, y2), (100,10,40), 2)
        length=boundRect[i][2]
        """мікро-перерва для відшивання ліній"""
        list.append((x1,y1,x2,y2,length))
        """закінчення набору списку прямокутників-обітків"""
cv2.imshow('Rt', gray)
"""початок розслідування"""
sorted=sorted(list,key=lambda line:line[4],reverse=True)
'''print(sorted)'''
x1,y1,x2,y2,dov=sorted[0]
'''print(x1,y1,x2,y2,dov)'''
cv2.rectangle(img, (x1, y1), (x2,y2), (100,10,40), 2)
crop = img[y1:y2, x1:x2]
crop=cv2.GaussianBlur(crop,(3,3),0)
crop_gray=cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(crop_gray, 170, 255, cv2.THRESH_BINARY_INV)
'''cv2.imshow("Area",thresh )'''

text = pytesseract.image_to_string(thresh, config='stdout -c tessedit_char_whitelist=0123456789')
print ("text-",text)

only_number = re.findall(r'\d,0', text)
only_number = ' '.join(map(str, only_number))
print(only_number)

contours2,_=cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for contour in contours2:
    x,y,w,h=cv2.boundingRect(contour)
    if w>10 and h>10:
        x=x+x1
        y=y+y1
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(img,only_number,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,0),2)

width = int(img.shape[1] * 0.5)
height = int(img.shape[0] * 0.5)
img= cv2.resize(img, (width, height) )

cv2.imshow('Result', img)
cv2.waitKey(0)