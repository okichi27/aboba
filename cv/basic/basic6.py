import cv2 
import numpy as np

input = np.array((
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 255, 255, 255, 0, 0, 0],
 [0, 255, 255, 255, 255, 255, 0, 0],
 [0, 255, 255, 0, 255, 255, 255, 0],
 [0, 255, 255, 255, 255, 255, 0, 0],
 [0, 0, 255, 255, 255, 0, 0, 0],
 [0,255, 0, 0, 0, 255, 0, 0],
 [0, 0, 255, 255, 255, 0, 0, 0]), dtype="uint8")

ker = np.array((
 [1, 1, 0],
 [0, -1, 0],
 [0, 1, 1]), dtype="int")

img = cv2.morphologyEx(input, cv2.MORPH_HITMISS, ker)

cv2.imshow("hit or miss", img)
cv2.imshow("original", input)

rate = 50
ker = (ker + 1) * 127
ker = np.uint8(ker)

cv2.imshow("ker", ker) 
cv2.waitKey(0)
