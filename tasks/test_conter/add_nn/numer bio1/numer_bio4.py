import cv2
import pytesseract
import numpy as np

img = cv2.imread('/home/rodion/yuliia0/aboba/tasks/task8/numer bio1/counter6.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

width = int(img.shape[1] * 2)
height = int(img.shape[0] * 2)
img= cv2.resize(img, (width, height) )

ker=np.ones((2,2),np.uint8)
img=cv2.erode(img, ker)
img=cv2.dilate(img,ker)
img=cv2.dilate(img,ker)

cv2.imshow('1', img)

'''img=cv2.GaussianBlur(img,(3,3),0)
ker=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
img=cv2.filter2D(img,-1,ker)'''

text = pytesseract.image_to_string(img, config='stdout -c tessedit_char_whitelist=0123456789')
print("text -",text[:-1])
for i, el in enumerate(text.splitlines()):
	if i == 0:
		continue

	el = el.split()
	try:
		# Создаем подписи на картинке
		x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
		cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
		cv2.putText(img, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
		print("next^",text[:-1])
	except IndexError:
		print("pass")


width = int(img.shape[1] * 0.5)
height = int(img.shape[0] * 0.5)
img= cv2.resize(img, (width, height) )

print("next^",text[:-1])
cv2.imshow('Result', img)
cv2.waitKey(0)