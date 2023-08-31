import numpy as np
import cv2
import glob
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((6*9,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)

objpoints = []
imgpoints = [] 
images = glob.glob('picture_chess*.jpg')
for fname in images:
 img = cv2.imread(fname)
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

 ret, corners = cv2.findChessboardCorners(gray, (9,6), None)

 if ret == True:
    objpoints.append(objp)
 corners2 = cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
 imgpoints.append(corners2)

 cv2.drawChessboardCorners(img, (9,6), corners2, ret)
 cv2.imshow('img', img)
 cv2.waitKey(30)

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
print(" Camera matrix:")
print(mtx)

print("\n Distortion coefficient:")
print(dist)

'''img = cv2.imread('/home/rodion/yuliia0/aboba/task7/picture_chess1.jpg')
h, w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult.jpg', dst)'''


n=0
image = glob.glob('*.png')
for name in image:
   imga = cv2.imread(name)
   n+=1
   h, w = imga.shape[:2]
   newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

   dst = cv2.undistort(imga, mtx, dist, None, newcameramtx)
   x, y, w, h = roi
   dst = dst[y:y+h, x:x+w]
   cv2.imwrite('calib2.1_{}.png'.format(n), dst)
'''   cv2.imshow('calib2.1_{}'.format(n), dst)'''
cv2.destroyAllWindows()