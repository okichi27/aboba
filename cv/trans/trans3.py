import cv2

img=cv2.imread("/home/rodion/yuliia0/aboba/cv/trans/my.jpg")

img =cv2.GaussianBlur(img, (3, 3),0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
x = cv2.Sobel(img, cv2.CV_8U, 1, 0, 3, 0, cv2.BORDER_REPLICATE)
y = cv2.Sobel(img, cv2.CV_8U, 0, 1, 3, 0, cv2.BORDER_REPLICATE) 
 
grad = cv2.addWeighted(x, 0.5, y, 0.5, 0)
 
cv2.imshow("2", grad)
cv2.waitKey(0)