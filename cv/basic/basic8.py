import cv2 

img = cv2.imread ("/home/rodion/yuliia0/aboba/cv/basic/cat.jpg")
rows, cols, _channels = map(int, img.shape)
cv2.imshow('original', img)
 
up = cv2.pyrUp(img, dstsize=(2 * cols, 2 * rows))
cv2.imshow("up", up)

down = cv2.pyrDown(img, dstsize=(cols // 2, rows // 2))
cv2.imshow("down", down)
cv2.waitKey (0)