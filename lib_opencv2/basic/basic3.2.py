import cv2
img= cv2.imread("/home/rodion/yuliia0/aboba/cv/basic/smoothing.jpg")
one =cv2.GaussianBlur(img, (3, 3), 0)
two =cv2.GaussianBlur(img, (15, 15), 0)
th =cv2.GaussianBlur(img, (21, 3), 0) 

cv2.imshow("orig", img)
cv2.imshow("one", one)
cv2.imshow("two", two)
cv2.imshow("rizni", th)
cv2.waitKey(0)
