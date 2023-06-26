import cv2


src = cv.imread(cv.samples.findFile(args.input))
if src is None:
 print('Could not open or find the image:', args.input)
 exit(0)

src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
dst = cv.equalizeHist(src)

cv.imshow('Source image', src)
cv.imshow('Equalized Image', dst)
cv.waitKey()