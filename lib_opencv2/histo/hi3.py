import cv2
import numpy as np

base = cv2.imread('/home/rodion/yuliia0/aboba/cv/histo/cat2.png')
test1 = cv2.imread('/home/rodion/yuliia0/aboba/cv/histo/cat3.jpg')
test2 = cv2.imread('/home/rodion/yuliia0/aboba/cv/histo/cat4.jpg')

hsv_base = cv2.cvtColor(base, cv2.COLOR_BGR2HSV)
hsv_test1 = cv2.cvtColor(test1, cv2.COLOR_BGR2HSV)
hsv_test2 = cv2.cvtColor(test2, cv2.COLOR_BGR2HSV)

hsv_half_down = hsv_base[hsv_base.shape[0]//2:,:]

histSize = [50, 60]
ranges = [0, 180] + [0, 256] 
channels = [0, 1]

hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

hist_half_down = cv2.calcHist([hsv_half_down], channels, None, histSize, ranges, accumulate=False)
cv2.normalize(hist_half_down, hist_half_down, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

hist_test1 = cv2.calcHist([hsv_test1], channels, None, histSize, ranges, accumulate=False)
cv2.normalize(hist_test1, hist_test1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

hist_test2 = cv2.calcHist([hsv_test2], channels, None, histSize, ranges, accumulate=False)
cv2.normalize(hist_test2, hist_test2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

for compare_method in range(4):
    base_base = cv2.compareHist(hist_base, hist_base, compare_method)
    base_half = cv2.compareHist(hist_base, hist_half_down, compare_method)
    base_test1 = cv2.compareHist(hist_base, hist_test1, compare_method)
    base_test2 = cv2.compareHist(hist_base, hist_test2, compare_method)

    print('Method:', compare_method, 'Perfect, Base-Half, Base-Test(1), Base-Test(2) :',\
          base_base, '/', base_half, '/', base_test1, '/', base_test2)
    