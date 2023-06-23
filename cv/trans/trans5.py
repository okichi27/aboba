import cv2
img=cv2.imread("/home/rodion/yuliia0/aboba/cv/trans/my.jpg")

img =cv2.GaussianBlur(img, (3, 3),0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
det = cv2.Canny(img, 5, 5*3, 3)

cv2.imshow("2", det)
cv2.waitKey(0)
