import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf


'''from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape(X_train.shape + (1,))
X_test = X_test.reshape(X_test.shape + (1, ))

X_train = X_train / 255.
X_test = X_test / 255.

X_train = X_train.astype(np.float32)
X_test = X_test.astype(np.float32)

from tensorflow.keras import layers

model = tf.keras.Sequential([
	layers.Conv2D(filters=10,
				kernel_size=3, 
				activation="relu", 
				input_shape=(28,  28,  1)),
	layers.Conv2D(10,  3, activation="relu"),
	layers.MaxPool2D(),
	layers.Conv2D(10,  3, activation="relu"),
	layers.Conv2D(10,  3, activation="relu"),
	layers.MaxPool2D(),
	layers.Flatten(),
	layers.Dense(10, activation="softmax")])

model.summary()

model.compile(loss="sparse_categorical_crossentropy", 
			optimizer=tf.keras.optimizers.Adam(),
			metrics=["accuracy"])

model.fit(X_train, y_train, epochs=10)
model.evaluate(X_test, y_test)

model.save("digit-recognizer.h5")'''

mnist =tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test)=mnist.load_data()

img = cv2.imread('/home/rodion/yuliia0/aboba/tasks/task8/numer bio1/lich4.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

model=tf.keras.models.load_model('handwritten.model')

prediction=model.predict(gray)
print(f"ths digit is probably a {{{np.argmax(prediction)}}}")
plt.imshow(gray[0],cmap=plt.cm.binary)
plt.show()
