import cv2 
img=cv2.imread("/home/rodion/yuliia0/aboba/cv/basic/smoothing.jpg")
cv2.imshow("original",img)
img = cv2.cvtColor (img, cv2.COLOR_BGR2HSV)
f = cv2.inRange (img, (50, 30, 50), (255, 255, 255))

cv2.imshow("inRange",f)
cv2.waitKey (0)