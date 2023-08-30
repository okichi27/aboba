from numpy import argmax
from keras.utils  import load_img
from keras.utils import img_to_array
from keras.models import load_model
import cv2

# load and prepare the image
def load_image(filename):
 # load the image
 img = load_img(filename, grayscale=True, target_size=(28, 28))
 # convert to array
 img = img_to_array(img)
 # reshape into a single sample with 1 channel
 img = img.reshape(1, 28, 28, 1)
 # prepare pixel data
 img = img.astype('float32')
 img = img / 255.0
 return img
 
original = cv2.imread('/home/rodion/yuliia0/aboba/tasks/task8/network.task8/network2.2/numer.task8.3.jpg')
cv2.imshow('zero', original)

img = load_image('/home/rodion/yuliia0/aboba/tasks/task8/network.task8/network2.2/numer.task8.3.jpg')

model = load_model('/home/rodion/yuliia0/aboba/tasks/task8/network.task8/network2.2/final_model.h5')
 # predict the class
predict_value = model.predict(img)
digit = argmax(predict_value)
print(digit)










'''# evaluate the deep model on the test dataset
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
 
# load train and test dataset
def load_dataset():
 # load dataset
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
 
# run the test harness for evaluating a model
def run_test_harness():
 # load dataset
 trainX, trainY, testX, testY = load_dataset()
 # prepare pixel data
 trainX, testX = prep_pixels(trainX, testX)
 # load model
 model = load_model('final_model.h5')
 # evaluate model on test dataset
 _, acc = model.evaluate(testX, testY, verbose=0)
 print('> %.3f' % (acc * 100.0))
 
# entry point, run the test harness
run_test_harness()'''

cv2.waitKey(0)