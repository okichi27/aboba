import cv2

img = cv2.imread("/home/rodion/yuliia0/aboba/cv/basic/cat.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("original", img)

n,dst = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
cv2.imshow("THRESH BINARY", dst)

n,dst = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("THRESH BINARY INV", dst)

n,dst = cv2.threshold(img, 30, 210, cv2.THRESH_TRUNC)
cv2.imshow("THRESH TRUNC", dst)

n,dst = cv2.threshold(img, 90, 240, cv2.THRESH_TOZERO)
cv2.imshow("THRESH TOZERO", dst)

n,dst = cv2.threshold(img, 30, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("THRESH TOZERO INV ", dst)

cv2.waitKey (0)