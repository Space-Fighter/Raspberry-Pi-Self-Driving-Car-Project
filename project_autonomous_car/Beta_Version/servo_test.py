from time import sleep
import RPi.GPIO as gpio
from keras.models import load_model
import cv2
import numpy as np

gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.OUT)
pwm = gpio.PWM(11,50)
pwm.start(90)

def set_angle (angle):
    duty = angle / 18 + 2
    gpio.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    gpio.output(11, False)
    pwm.ChangeDutyCycle(90)


def img_preprocess(img):
    img = img[60:135,:]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img,  (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img/255
    return img

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    frame = np.asarray(frame)
    print(frame.shape)
    frame = img_preprocess(frame)
    frame = np.array([frame])
    print('Frame shape: ' + str(frame.shape))
    cap.release()
    return frame
def steer(steering_angle):
    if steering_angle > 0:
        print('Move Right')
    else:
        print('Move Left')
    angle = int(steering_angle)
    angle = -1 * steering_angle
    angle = 90 + angle
    if angle in [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 0]:
        set_angle(90)
    else:
        set_angle(angle)
    set_angle(90)
    time.sleep(0.01)
    pwm.stop
    gpio.cleanup()
    gpio.setmode(gpio.BOARD)
    gpio.setup(11,gpio.OUT)
    pwm = gpio.PWM(11,50)
    pwm.start(90)

model = load_model('model3.h5')
print('Sucessfully loaded model sir, please don\'t worry the above lines are not errors, they are warnings')
while True:
    frame = capture_image()
    steering_angle = float(model.predict(frame))
    print('Steering_angle:'+ str(int(steering_angle, 0)))
    steer(steering_angle)
