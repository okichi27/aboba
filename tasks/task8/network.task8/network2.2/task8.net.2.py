
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
 
def load_dataset():
 (trainX, trainY), (testX, testY) = mnist.load_data()
 # reshape dataset to have a single channel
 trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
 testX = testX.reshape((testX.shape[0], 28, 28, 1))
 # one hot encode target values
 trainY = to_categorical(trainY)
 testY = to_categorical(testY)
 return trainX, trainY, testX, testY
 
# scale pixels
def prep_pixels(train, test):
 # convert from integers to floats
 train_norm = train.astype('float32')
 test_norm = test.astype('float32')
 # normalize to range 0-1
 train_norm = train_norm / 255.0
 test_norm = test_norm / 255.0
 # return normalized images
 return train_norm, test_norm
 
# define cnn model
def define_model():
 model = Sequential()
 model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
 model.add(MaxPooling2D((2, 2)))
 model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
 model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
 model.add(MaxPooling2D((2, 2)))
 model.add(Flatten())
 model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
 model.add(Dense(10, activation='softmax'))
 # compile model
 opt = SGD(learning_rate=0.01, momentum=0.9)
 model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
 return model
 
# run the test harness for evaluating a model
def run_test_harness():
 # load dataset
 trainX, trainY, testX, testY = load_dataset()
 # prepare pixel data
 trainX, testX = prep_pixels(trainX, testX)
 # define model
 model = define_model()
 # fit model
 model.fit(trainX, trainY, epochs=10, batch_size=32, verbose=0)
 # save model
 model.save('final_model.h5')
 
# entry point, run the test harness
run_test_harness()




'''@pytest.mark.mpi
def test_mpi():
    pass'''

'''import h5py
h5py.run_tests()'''


'''__author__ = 'anish'

import cv2
import numpy as np
import  imutils


img_org = cv2.imread('/home/rodion/yuliia0/aboba/tasks/task8/numer_car/car_numer5.jpg')
size = np.shape(img_org)
if size[0] <= 776:
    img_org = imutils.resize(img_org , 900)

img_org2 = img_org.copy()
img_bw = cv2.cvtColor(img_org , cv2.COLOR_BGR2GRAY)


ret3,img_thr = cv2.threshold(img_bw,125,255,cv2.THRESH_BINARY)


img_edg  = cv2.Canny(img_thr ,100,200)

cv2.imshow('canny',img_edg)

kernel = cv2.getStructuringElement(cv2.MORPH_DILATE, (7, 7))
img_dil = cv2.dilate(img_edg, kernel, iterations = 1)

contours ,hierarchye = cv2.findContours(img_edg, 1, 2)
print(contours)
cnts = sorted(contours, key = cv2.contourArea, reverse = True)[:10]

screenCnt = None

for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)

	# if our approximated contour has four points, then
	# we can assume that we have found our screen
	if len(approx) == 4:
		screenCnt = approx
		print('screenCnt',screenCnt)
		break
	    


mask = np.zeros(img_bw.shape, dtype=np.uint8)
print(screenCnt)

roi_corners = np.array(screenCnt ,dtype=np.int32)
ignore_mask_color = (255,0,0)*1
cv2.fillPoly(mask, roi_corners , ignore_mask_color)
cv2.drawContours(img_org, [screenCnt], -40, (100, 255, 100), 9)
cv2.imshow('original  image with boundry' , img_org)
cv2.imwrite('plate_detedted.jpg',img_org)


ys =[screenCnt[0,0,1] , screenCnt[1,0,1] ,screenCnt[2,0,1] ,screenCnt[3,0,1]]
xs =[screenCnt[0,0,0] , screenCnt[1,0,0] ,screenCnt[2,0,0] ,screenCnt[3,0,0]]

ys_sorted_index = np.argsort(ys)
xs_sorted_index = np.argsort(xs)

x1 = screenCnt[xs_sorted_index[0],0,0]
x2 = screenCnt[xs_sorted_index[3],0,0]

y1 = screenCnt[ys_sorted_index[0],0,1]
y2 = screenCnt[ys_sorted_index[3],0,1]



img_plate = img_org2[y1:y2 , x1:x2]


for i in screenCnt:
    print(i)

    print (x1,x2,y1,y2)

cv2.imshow('number plate',img_plate)

cv2.imwrite('number_plate.jpg',img_plate)
cv2.waitKey(0)'''