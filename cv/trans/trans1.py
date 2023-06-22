import cv2
import numpy as np
img=cv2.imread("/home/rodion/yuliia0/aboba/cv/trans/dog.jpg")
cv2.imshow ("original", img)

ker = np.ones((3, 3), dtype=np.float32)
ker /= (3 * 3)
dst = cv2.filter2D (img, -1, ker)
cv2.imshow ("ker 3", dst)

ker = np.ones((7, 7), dtype=np.float32)
ker /= (7 * 7)
dst = cv2.filter2D (img, -1, ker)
cv2.imshow ("ker 7", dst)

ker = np.ones((11, 11), dtype=np.float32)
ker /= (11 * 11)
dst = cv2.filter2D (img, -1, ker)
cv2.imshow ("ker 11", dst)

cv2.waitKey (0)