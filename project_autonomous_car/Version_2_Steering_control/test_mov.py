import pynput
from pynput.keyboard import Key, Listener
import pandas as pd
import cv2
import mov
import RPi.GPIO as gpio
from threading import Thread
servo_pos = 90
mov.steer(90)

keys = {
    Key.up: False,
    Key.down: False,
    Key.left: False,
    Key.right: False
}


def on_press(key):
    global servo_pos, keys
    if key in keys:
        keys[key] = True


def on_release(key):
    global servo_pos, keys
    if key in keys:
        keys[key] = False
        servo_pos = 90

def keyboard_listener():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


Thread(target=keyboard_listener, daemon=True).start()

while True:
    print('Started to work')
    if keys[Key.up] and keys[Key.right]:
        if servo_pos >= 55 and servo_pos < 91:
            servo_pos -= 2.5
            mov.steer(servo_pos)
            mov.forward()
    
        elif servo_pos < 55:
            mov.steer(55)
            mov.forward()
            servo_pos = 55
    
    elif keys[Key.up] and keys[Key.left]:
        if servo_pos <= 130:
            servo_pos +=2.5
            mov.steer(servo_pos)
            mov.forward()
        if servo_pos > 130:
            mov.steer(130)
            mov.forward()
            servo_pos = 130
    elif keys ==  Key.up:
        mov.forward()
        gpio.cleanup()
        mov.init()

    elif keys == Key.down:
        mov.reverse()
        gpio.cleanup()
        mov.init()

    elif keys == Key.left:
        servo_pos +=1
        if servo_pos <= 130:
            mov.steer(servo_pos)
        if servo_pos > 130:
            mov.steer(130)

    elif keys == Key.right:
        servo_pos -=1
        if servo_pos >= 55 and servo_pos < 91:
            mov.steer(servo_pos)
        if servo_pos < 55:
            mov.steer(50)
    else:
        servo_pos = 90
        mov.steer(servo_pos)        
#    if key == Key.right:
#        servo_pos -=1
#        if servo_pos >= 55 and servo_pos < 91:
#            mov.steer(servo_pos)
#        if servo_pos < 55:
#            mov.steer(50)
        
#    global servo_pos
#    if key ==  Key.up:
#        mov.forward()
#        gpio.cleanup()
#        mov.init()
#    if key == Key.down:
#        mov.reverse()
#        gpio.cleanup()
#        mov.init()
#    if key == Key.left:
#        servo_pos +=1
#        if servo_pos <= 130:
#            mov.steer(servo_pos)
#        if servo_pos > 130:
#            mov.steer(130)
#                          
#    if key == Key.right:
#        servo_pos -=1
#        if servo_pos >= 55 and servo_pos < 91:
#            mov.steer(servo_pos)
#        if servo_pos < 55:
#            mov.steer(50)
#    if any([key in COMBO for COMBO in COMBINATIONS]):
#        current.add(key)
#
#        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
#                    print('worked')
