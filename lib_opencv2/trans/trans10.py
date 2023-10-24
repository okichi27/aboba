import cv2 as cv
import numpy as np

img = cv.imread("/home/rodion/yuliia0/aboba/cv/trans/my.jpg")

im = np.array( [[0, 0], [img.shape[1] - 1, 0], [0, img.shape[0] - 1]] ).astype(np.float32)
i = np.array( [[0, img.shape[1]*0.3], [img.shape[1]*0.8, img.shape[0]*0.5], [img.shape[1]*0.5, img.shape[0]*0.7]] ).astype(np.float32)
war= cv.getAffineTransform(im, i)
warp= cv.warpAffine(img, war, (img.shape[1], img.shape[0]))

center = (warp.shape[1]//2, warp.shape[0]//2)

rot= cv.getRotationMatrix2D( center, 250, 1 )
warpr = cv.warpAffine(warp, rot, (warp.shape[1], warp.shape[0]))
cv.imshow('original', img)
cv.imshow('warp', warp)
cv.imshow('warp and rotate', warpr)
cv.waitKey()