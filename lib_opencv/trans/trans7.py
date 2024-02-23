import cv2

img=g=cv2.imread("/home/rodion/yuliia0/aboba/cv/trans/tr.jpg")
cv2.imshow("original", img)

img = cv2.GaussianBlur(img, (3, 3),0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img  = cv2.resize(img, (1280, 720))
g = cv2.resize(g, (1280, 720))
rows = img.shape[0]
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=30, minRadius=1, maxRadius=30000)

for i in circles[0, :]:
  cv2.circle(g, (int(i[0]), int(i[1])), int(i[2]), (0, 0, 255), 3)

cv2.imshow("2", g)
cv2.waitKey(0)