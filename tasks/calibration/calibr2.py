import cv2
import numpy as np


import glob

CHECKERBOARD = (6, 9)

criteria = (cv2.TERM_CRITERIA_EPS +
			cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)


threedpoints = []

twodpoints = []

objectp3d = np.zeros((1, CHECKERBOARD[0]
					* CHECKERBOARD[1],
					3), np.float32)
objectp3d[0, :, :2] = np.mgrid[0:CHECKERBOARD[0],
							0:CHECKERBOARD[1]].T.reshape(-1, 2)
prev_img_shape = None

images = glob.glob('*.png')

for filename in images:
	image = cv2.imread(filename)
	grayColor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	ret, corners = cv2.findChessboardCorners(
					grayColor, CHECKERBOARD,
					cv2.CALIB_CB_ADAPTIVE_THRESH
					+ cv2.CALIB_CB_FAST_CHECK +
					cv2.CALIB_CB_NORMALIZE_IMAGE)

	if ret == True:
		threedpoints.append(objectp3d)

		corners2 = cv2.cornerSubPix(
			grayColor, corners, (11, 11), (-1, -1), criteria)

		twodpoints.append(corners2)

		image = cv2.drawChessboardCorners(image,
										CHECKERBOARD,
										corners2, ret)

	cv2.imshow('img', image)
	cv2.waitKey(0)

cv2.destroyAllWindows()

h, w = image.shape[:2]

ret, matrix, distortion, r_vecs, t_vecs = cv2.calibrateCamera(
	threedpoints, twodpoints, grayColor.shape[::-1], None, None)

print(" Camera matrix:")
print(matrix)

print("\n Distortion coefficient:")
print(distortion)

print("\n Rotation Vectors:")
print(r_vecs)

print("\n Translation Vectors:")
print(t_vecs)
