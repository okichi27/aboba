import cv2
import numpy as np

numer=0
digits = []
list=[0,1,2,3,4,5,6,7,8,9]
'''цифри'''
while numer<len(list):
    digit=str(list[numer])
    (width, height), bline = cv2.getTextSize(digit, cv2.FONT_HERSHEY_SIMPLEX,3, 5)
    digits.append(np.zeros((height, width), np.uint8))
    cv2.putText(digits[-1], digit, (0, height), cv2.FONT_HERSHEY_SIMPLEX,3, (255, 255, 255), 5)
    x0, y0, w, h = cv2.boundingRect(digits[-1])
    digits[-1] = digits[-1][y0:y0+h, x0:x0+w]
    cv2.imwrite("{}_numer.jpg".format(numer),digits[-1])
    numer+=1

cv2.destroyAllWindows()