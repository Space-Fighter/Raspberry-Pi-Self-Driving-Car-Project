#import movements
#from keras.models import load_model
import cv2
import matplotlib.pyplot as plt
#import numpy as np
#import movements as mov
def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    print('Frame shape: ' + str(frame.shape))
    cap.release()
    return frame

frame = capture_image()
plt.imshow(frame)
plt.show()
