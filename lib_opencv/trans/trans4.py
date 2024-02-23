import cv2

img=cv2.imread("/home/rodion/yuliia0/aboba/cv/trans/my.jpg")

img =cv2.GaussianBlur(img, (3, 3),0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = cv2.Laplacian(img, cv2.CV_8U, 5)

dst = cv2.convertScaleAbs(dst)
 
cv2.imshow("2", dst)
cv2.waitKey(0)