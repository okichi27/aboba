import cv2

img=cv2.imread("/home/rodion/yuliia0/aboba/cv/trans/my.jpg")
cv2.imshow ("original", img)

bottom =top = int(0.05 * img.shape[0])
right =left = int(0.05 * img.shape[1])
 
dst = cv2.copyMakeBorder(img, top, bottom, left, right,cv2.BORDER_CONSTANT, None, [150,150,10])
cv2.imshow("ker 11", dst)

dst = cv2.copyMakeBorder(img, top, bottom, left, right,cv2.BORDER_REPLICATE, None, [100,150,150])
cv2.imshow("ker 12", dst)

cv2.waitKey(0)