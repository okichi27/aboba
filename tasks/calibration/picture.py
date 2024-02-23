import cv2
import numpy as np

cap1 = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

frame_numer = 1
n=0
while(True):
    ret1, frame1 = cap1.read()
    frame1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame1)
    if cv2.waitKey(1)== ord("q"):
       break
    if frame_numer%20==0:
        n+=1
        cv2.imwrite("/home/rodion/yuliia0/aboba/task7/{}_picture.jpg".format(n),frame1)
        print('n=',n)
    frame_numer += 1
    print(frame_numer)

cap1.release()

cv2.destroyAllWindows()