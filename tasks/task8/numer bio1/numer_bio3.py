from PIL import Image
import cv2
import pytesseract

img = Image.open('/home/rodion/yuliia0/aboba/tasks/task8/numer bio1/counter6.jpg')

text = pytesseract.image_to_string(img, config='--psm 6')


imga = cv2.imread('/home/rodion/yuliia0/aboba/tasks/task8/numer bio1/counter6.jpg')

text1 = pytesseract.image_to_string(imga, config='--psm 6')

print('1 -',text,"next 1:")
print(text1)