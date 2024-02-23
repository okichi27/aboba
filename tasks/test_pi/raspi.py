import cv2
import numpy as np

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(2)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out1 = cv2.VideoWriter('biba.mp4', fourcc, 15, (640,480))
out2 = cv2.VideoWriter('bibka.mp4', fourcc, 15, (640,480))

frame_numer = 0
while(frame_numer<80):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    print(frame1.shape)
    print(frame2.shape)
    if frame_numer>=0:
       frame_1=frame1
       frame_2=frame2
    if frame_numer>20:
       frame_1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
       frame_2=cv2.cvtColor(frame2,cv2.COLOR_RGB2BGR)
    if frame_numer>39:
       frame_1=cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)
       ker=np.ones((4,4),np.uint8)
       frame_1=cv2.erode(frame_1,ker)
       frame_2=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
       '''frame_2=cv2.morphologyEx(frame_2,cv2.MORPH_OPEN,(5,5))'''
    if frame_numer>60:
       frame_1=cv2.blur(frame1,(5,5))
       frame_1=cv2.putText(frame_1,"biba",(220,650),cv2.FONT_HERSHEY_SIMPLEX,2,(200,90,70),5,cv2.LINE_AA)
       frame_2=cv2.flip(frame2,0)
       '''frame_2=(frame_2,-1,1,1)'''
    #cv2.imshow('frame', frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #  break
    #if cv2.waitKey(1) == ord('w'):
    #  frame=cv2.resize(frame,(128*4,72*4))
    #  cv2.imshow('frame_picture', frame)
    if frame_numer==40:
      cv2.imwrite("picture_biba{}.jpg".format(frame_numer),frame_1)
      cv2.imwrite("picture_bibka{}.jpg".format(frame_numer),frame_2)
    out1.write(frame_1)
    out2.write(frame_2)
    frame_numer += 1
    print(frame_numer)

cap1.release()
out1.release()
cap2.release()
out2.release()
cv2.destroyAllWindows()