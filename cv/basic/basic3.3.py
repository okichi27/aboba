import cv2
img= cv2.imread("/home/rodion/yuliia0/aboba/cv/basic/smoothing.jpg")
one =cv2.medianBlur(img, 3)
two =cv2.medianBlur(img, 9)
th =cv2.medianBlur(img, 21)

cv2.imshow("orig", img)
cv2.imshow("one", one)
cv2.imshow("two", two)
cv2.imshow("th", th)
cv2.waitKey(0)