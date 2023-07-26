import cv2
import numpy as np

img = cv2.imread('/home/rodion/yuliia0/aboba/cv/histo/cat2.png')
templ = cv2.imread('/home/rodion/yuliia0/aboba/cv/histo/templ.jpg')
img_display = img.copy()
cv2.imshow("biba", img)
cv2.imshow('templ', templ)

mask=cv2.cvtColor(templ, cv2.COLOR_BGR2GRAY)
ker=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
mask=cv2.filter2D(mask,-1,ker)
cv2.imshow('mask', mask)

result=cv2.matchTemplate(img,templ, cv2.TM_SQDIFF)
_minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(result, None)
cv2.rectangle(img_display, minLoc, (minLoc[0] + templ.shape[0], minLoc[1] + templ.shape[1]), (255,255,255), 2, 8, 0 )
cv2.rectangle(result, minLoc, (minLoc[0] + templ.shape[0], minLoc[1] + templ.shape[1]), (255,255,255), 2, 8, 0 )
cv2.imshow('1', result)

result=cv2.matchTemplate(img,templ, cv2.TM_SQDIFF_NORMED)
_minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(result, None)
cv2.rectangle(img_display, minLoc, (minLoc[0] + templ.shape[0], minLoc[1] + templ.shape[1]), (255,255,255), 2, 8, 0 )
cv2.rectangle(result, minLoc, (minLoc[0] + templ.shape[0], minLoc[1] + templ.shape[1]), (255,255,255), 2, 8, 0 )
cv2.imshow('2', result)

result=cv2.matchTemplate(img,templ, cv2.TM_SQDIFF_NORMED, mask)
_minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(result, None)
cv2.rectangle(img_display, minLoc, (minLoc[0] + templ.shape[0], minLoc[1] + templ.shape[1]), (255,255,255), 2, 8, 0 )
cv2.rectangle(result, minLoc, (minLoc[0] + templ.shape[0], minLoc[1] + templ.shape[1]), (255,255,255), 2, 8, 0 )
cv2.imshow('2+mask', result)

result=cv2.matchTemplate(img,templ, cv2.TM_CCORR)
_minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(result, None)
cv2.rectangle(img_display, minLoc, (minLoc[0] + templ.shape[0], minLoc[1] + templ.shape[1]), (255,255,255), 2, 8, 0 )
cv2.rectangle(result, minLoc, (minLoc[0] + templ.shape[0], minLoc[1] + templ.shape[1]), (255,255,255), 2, 8, 0 )
cv2.imshow('3', result)

result=cv2.matchTemplate(img,templ, cv2.TM_CCORR_NORMED)
_minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(result, None)
cv2.rectangle(img_display, maxLoc, (maxLoc[0] + templ.shape[0], maxLoc[1] + templ.shape[1]), (255,255,255), 2, 8, 0 )
cv2.rectangle(result, maxLoc, (maxLoc[0] + templ.shape[0], maxLoc[1] + templ.shape[1]), (255,255,255), 2, 8, 0 )
cv2.imshow('4', result)

result=cv2.matchTemplate(img,templ, cv2.TM_CCOEFF)
_minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(result, None)
cv2.rectangle(img_display, maxLoc, (maxLoc[0] + templ.shape[0], maxLoc[1] + templ.shape[1]), (255,255,255), 2, 8, 0 )
cv2.rectangle(result, maxLoc, (maxLoc[0] + templ.shape[0], maxLoc[1] + templ.shape[1]), (255,255,255), 2, 8, 0 )
cv2.imshow('5', result)

result=cv2.matchTemplate(img,templ, cv2.TM_CCOEFF_NORMED)
_minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(result, None)
cv2.rectangle(img_display, maxLoc, (maxLoc[0] + templ.shape[0], maxLoc[1] + templ.shape[1]), (255,255,255), 2, 8, 0 )
cv2.rectangle(result, maxLoc, (maxLoc[0] + templ.shape[0], maxLoc[1] + templ.shape[1]), (255,255,255), 2, 8, 0 )
cv2.imshow('6', result)

cv2.waitKey(0)