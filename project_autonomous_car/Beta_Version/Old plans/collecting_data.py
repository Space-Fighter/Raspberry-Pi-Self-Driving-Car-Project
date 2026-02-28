import picamera
import time
import cv2
import sys
import numpy as np



def key_input(event):
    init()
    print('Key:', event.char)
    key_press = event.char
    gpio.setmode(gpio.BCM)
    gpio.setup(16, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    gpio.setup(25, gpio.OUT)

    if key_press.lower() == 'w':
        forward()
    elif key_press.lower() == 's':
        reverse()
    elif key_press.lower() == 'a':
        left()
    elif key_press.lower() == 'd':
        right()
    elif key_press.lower() == 'e':
        gpio.cleanup()
        return 'done'
    else:
        gpio.cleanup()
















def process_img(image):
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1 = 200, threshold2 = 300)
    return processed

camera = picamera.PiCamera()
camera.capture(output = img, format ='jpeg')
time.sleep(0.0001)
img = cv2.imread(img)
img = process_img(img)
cv2.imshow('img', img)
cv2.waitKey(1)
if cv2.waitKey(25) & 0xFF == ord('q'):
    cv2.destroyAllWindows()



##cap = cv2.VideoCapture(0)
##
##while(True):
##    ret, frame = cap.read()
##    img = frame
##
##    cv2.imshow('frame',img)
##    cv2.waitKey(1)
##    if cv2.waitKey(1) & 0xFF == ord('q'):
##        break
##cap.release()


##
##from io import BytesIO
##from time import sleep
##from picamera import PiCamera
##from PIL import Image
##
### Create the in-memory stream
##stream = BytesIO()
##camera = PiCamera()
##camera.start_preview()
##sleep(2)
##camera.capture(stream, format='jpeg')
### "Rewind" the stream to the beginning so we can read its content
##stream.seek(0)
##image = Image.open(stream)
