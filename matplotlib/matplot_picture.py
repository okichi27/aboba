import cv2
import numpy as np
from matplotlib import pyplot as plt
 
 
img = cv2.imread('/home/rodion/yuliia0/aboba/matplotlib/picture_pipka.jpg')
rows, cols, ch = img.shape
 
pts1 = np.float32([[50, 50],
                   [200, 50],
                   [50, 200]])
 
pts2 = np.float32([[10, 100],
                   [200, 50],
                   [100, 250]])
 
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))
 
plt.subplot(121)
plt.imshow(img)
plt.title('Input')
 
plt.subplot(122)
plt.imshow(dst)
plt.title('Output')
 
plt.show()
 
# Displaying the image
while(1):
     
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
         
cv2.destroyAllWindows()