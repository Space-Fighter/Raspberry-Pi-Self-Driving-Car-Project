import pynput
from pynput.keyboard import Key, Listener
import pandas as pd
import cv2
from threading import Thread
import time
# import mov
#import RPi.GPIO as gpio


keys = {
    Key.up: False,
    Key.down: False,
    Key.left: False,
    Key.right: False
}


def on_press(key):
    if key in keys:
        keys[key] = True


def on_release(key):
    if key in keys:
        keys[key] = False


def keyboard_listener():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


Thread(target=keyboard_listener, daemon=True).start()

while True:
    if keys[Key.up] and keys[Key.right]:
        print('Might have worked well')
    elif keys[Key.left]:
        print('Might have worked')
    time.sleep(0.1)
    
    
'''
import pynput
from pynput.keyboard import Key, Listener
import pandas as pd
import cv2
import mov
import RPi.GPIO as gpio

servo_pos = 90
mov.steer(90)
COMBINATIONS = [
    {Key.up, Key.right},
    {Key.up, Key.left}
]

keys = {
    Key.up: False,
    Key.down: False,
    Key.left: False,
    Key.right: False
}


def on_press(key):
    if key in keys:
        keys[key] = True


def on_release(key):
    if key in keys:
        keys[key] = False


def keyboard_listener():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


Thread(target=keyboard_listener, daemon=True).start()

while True:
    if keys[Key.up] and keys[Key.right]:
        print('Might have worked well')
    
    if keys[Key.up] and keys[Key.left]:
        print('Might have worked well')
    
    if keys[Key.right]:
        print('Might have worked')
    if keys[Key.left]:
        print('Might have worked')
    time.sleep(0.1)
'''