import cv2
img= cv2.imread("/home/rodion/yuliia0/aboba/cv/basic/basic3.2.png")
one =cv2.bilateralFilter(img, 2, 2 * 2, 2 / 2)
two =cv2.bilateralFilter(img, 1, 1 * 2, 1 / 2)
th =cv2.bilateralFilter(img, 2, 3 * 2, 8 / 2)

cv2.imshow("orig", img)
cv2.imshow("one", one)
cv2.imshow("two", two)
cv2.imshow("th", th)
cv2.waitKey(0)