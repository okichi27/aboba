import cv2
import numpy as np

imgIn = cv2.imread("/home/rodion/yuliia0/aboba/cv/others/biba.jpg")
w=52
C_Thr = 0.43
LowThr = 35
HighThr = 57
def calcGST(imgIn,w):
 img = imgIn.astype(np.float32)

 imgDiffX = cv2.Sobel(img, cv2.CV_32F, 1, 0, 3)
 imgDiffY = cv2.Sobel(img, cv2.CV_32F, 0, 1, 3)
 imgDiffXY = cv2.multiply(imgDiffX, imgDiffY)
 
 imgDiffXX = cv2.multiply(imgDiffX, imgDiffX)
 imgDiffYY = cv2.multiply(imgDiffY, imgDiffY)
 J11 = cv2.boxFilter(imgDiffXX, cv2.CV_32F, (52,52))
 J22 = cv2.boxFilter(imgDiffYY, cv2.CV_32F, (52,52))
 J12 = cv2.boxFilter(imgDiffXY, cv2.CV_32F, (52,52))

 tmp1 = J11 + J22
 tmp2 = J11 - J22
 tmp2 = cv2.multiply(tmp2, tmp2)
 tmp3 = cv2.multiply(J12, J12)
 tmp4 = np.sqrt(tmp2 + 4.0 * tmp3)
 lambda1 = 0.5*(tmp1 + tmp4)
 lambda2 = 0.5*(tmp1 - tmp4)
 imgCoherencyOut = cv2.divide(lambda1 - lambda2, lambda1 + lambda2)

 imgOrientationOut = cv2.phase(J22 - J11, 2.0 * J12, angleInDegrees = True)
 imgOrientationOut = 0.5 * imgOrientationOut


imgCoherency, imgOrientation = calcGST(imgIn, 52)
_, imgCoherencyBin = cv2.threshold(imgCoherency, C_Thr, 255, cv2.THRESH_BINARY)
_, imgOrientationBin = cv2.threshold(imgOrientation, LowThr, HighThr, cv2.THRESH_BINARY)
imgBin = cv2.bitwise_and(imgCoherencyBin, imgOrientationBin)
imgCoherency = cv2.normalize(imgCoherency, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
imgOrientation = cv2.normalize(imgOrientation, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
cv2.imshow('result.jpg', np.uint8(0.5*(imgIn + imgBin)))
cv2.imshow('Coherency.jpg', imgCoherency)
cv2.imshow('Orientation.jpg', imgOrientation)
cv2.waitKey(0)