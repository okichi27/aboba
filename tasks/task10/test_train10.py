"""
import cv2

original = cv2.imread('/home/rodion/yuliia0/aboba/tasks/task10.net/data/training_images/vid_4_740.jpg')

x1=4
y1=203
x2=199
y2=276

cv2.imwrite("/home/rodion/yuliia0/aboba/tasks/task10.net/test10/train/train.4.jpg", original)
orig=cv2.rectangle(original, (int(x1), int(y1)), (int(x2), int(y2)), (160,10,140), 2)

width=str(((x2-x1))/original.shape[1])
height=str(((y2-y1))/original.shape[0])
x_center=str(((x2-x1)/2+x1)/original.shape[1])
y_center=str(((y2-y1)/2+y1)/original.shape[0])
class_1=str(0)


with open('/home/rodion/yuliia0/aboba/tasks/task10.net/test10/labels/annotations.4.txt', 'a') as f:
    f.write(' '. join ([(class_1),(x_center),(y_center),(width),(height)]))

cv2.imshow('result', orig)
cv2.waitKey(0)
"""


f = open()



































'''import cv2

original = cv2.imread('/home/rodion/yuliia0/aboba/tasks/task10.net/data/training_images/vid_4_700.jpg')

x1=250.4428365
y1=197.3053411
x2=510.1794501
y2=283.3799871

cv2.imwrite("/home/rodion/yuliia0/aboba/tasks/task10.net/test10/train/train.3.jpg", original)
orig=cv2.rectangle(original, (int(x1), int(y1)), (int(x2), int(y2)), (160,10,140), 2)

width=str(((x2-x1))/original.shape[1])
height=str(((y2-y1))/original.shape[0])
x_center=str(((x2-x1)/2+x1)/original.shape[1])
y_center=str(((y2-y1)/2+y1)/original.shape[0])
class_1=str(0)


with open('/home/rodion/yuliia0/aboba/tasks/task10.net/test10/labels/annotations.3.txt', 'a') as f:
    f.write(' '. join ([str(class_1),str(x_center),str(y_center),str(width),(height)])+'/n')
    f.write(' '. join ([class_1,x_center,y_center,width,height]))

cv2.imshow('result', orig)
cv2.waitKey(0)'''