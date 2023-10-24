import cv2
img= cv2.imread("/home/rodion/yuliia0/aboba/cv/basic/smoothing.jpg")
one = cv2.blur(img, (3, 3))
two = cv2.blur(img, (7, 7))
th = cv2.blur(img, (19, 1))

cv2.imshow("orig", img)
cv2.imshow("one", one)
cv2.imshow("two", two)
cv2.imshow("rizni", th)
cv2.waitKey(0)
