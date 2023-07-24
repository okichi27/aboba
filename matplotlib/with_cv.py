import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

while cap.isOpened():
    ret, frame = cap.read()
    frame_new =cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    plt.imshow(frame_new)
    plt.axis('off')
    plt.show()
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('pipka.mp4', fourcc, 15, (640, 480))

while(True):
	# reads frames from a camera
	# ret checks return at each frame
	ret, frame = cap.read()

	# Converts to HSV color space, OCV reads colors as BGR
	# frame is converted to hsv
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	# output the frame
	out.write(hsv)
	
	# The original input frame is shown in the window
	cv2.imshow('Original', frame)

	# The window showing the operated video stream
	cv2.imshow('frame', hsv)

	
	# Wait for 'a' key to stop the program
	if cv2.waitKey(1) & 0xFF == ord('a'):
		break

# Close the window / Release webcam
cap.release()

# After we release our webcam, we also release the output
out.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()'''
