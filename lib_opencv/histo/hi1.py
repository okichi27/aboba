import cv2

img = cv2.imread("/home/rodion/yuliia0/aboba/cv/histo/cat2.png")
cv2.imshow('original', img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', img)

img = cv2.equalizeHist(img)

cv2.imshow('histo 1', img)
cv2.waitKey(0)