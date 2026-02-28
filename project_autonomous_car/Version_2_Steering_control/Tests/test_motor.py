import RPi.GPIO as gpio
import time
import tkinter as tk
import sys


# Motor controller pin setup
gpio.setmode(gpio.BOARD)
gpio.setup(3, gpio.OUT)
gpio.setup(5, gpio.OUT)
gpio.setup(7, gpio.OUT)
gpio.setup(8, gpio.OUT)

# Servo pins setup
gpio.setup(12,gpio.OUT)
pwm = gpio.PWM(12,80)
pwm.start(0)

def reset():
    gpio.cleanup()
    gpio.setmode(gpio.BOARD)
    gpio.setup(3, gpio.OUT)
    gpio.setup(5, gpio.OUT)
    gpio.setup(7, gpio.OUT)
    gpio.setup(8, gpio.OUT)

    # Servo pins setup
    gpio.setup(10,gpio.OUT)
    pwm = gpio.PWM(10,80)
    pwm.start(0)


def forward():
    # 4 wheel drive(forward)
    gpio.output(3,  False)
    gpio.output(5, True)
    gpio.output(7, False)
    gpio.output(8, True)
    time.sleep(0.03)


def reverse():
    # 4 wheel drive(forward)
    gpio.output(3,  True)
    gpio.output(5, False)
    gpio.output(7, True)
    gpio.output(8, False)
    time.sleep(0.03)


def steer(angle):
    # red wire in + 5V slot which is pin number 2
    # black wire in gnd or ground slot which is pin number 9
    # white wire signal is in gpio slot which is pin number 10 gpio 16 -
    duty = angle / 18 + 2
    gpio.output(10, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    gpio.output(10, False)

def key_input(event):
    print('Key:', event.char)
    reset()
    key_press = event.char
    if key_press.lower() == 'w':
        forward()
    elif key_press.lower() == 's':
        reverse()
    elif key_press.lower() == 'a':
        steer(115)
    elif key_press.lower() == 'd':
        steer(65)
    pwm.stop()
    gpio.cleanup()
try:
    root = tk.Tk()
    root.bind('<KeyPress>', key_input)
    root.mainloop()
except:
    gpio.cleanup

