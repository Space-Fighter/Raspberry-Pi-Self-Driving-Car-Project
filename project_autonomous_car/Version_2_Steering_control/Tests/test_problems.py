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

print('Started to work')
Thread(target=keyboard_listener, daemon=True).start()

for i in range(1000000000000):
    if keys[Key.up] and keys[Key.right]:
        servo_pos -= 1
        if servo_pos >= 55 and servo_pos < 91:
            mov.steer(servo_pos)
            mov.forward()
            print('Key right, Key up combination', servo_pos)
        elif servo_pos < 55:
            mov.steer(55)
            mov.forward()
            print('Key right, Key up combination============1', servo_pos)
            servo_pos = 55
            print('Key right, Key up combination |\|\|\|\|\|\|2', servo_pos)
        mov.stop()
            
    elif keys[Key.up] and keys[Key.left]:
        servo_pos +=1
        if servo_pos <= 130:
            mov.steer(servo_pos)
            mov.forward()
            print('key left, Key up combination', servo_pos)
        if servo_pos > 130:
            mov.steer(130)
            mov.forward()
            print('Key right, Key up combination============1', servo_pos)
            servo_pos = 130
            print('Key right, Key up combination |\|\|\|\|\|\|2', servo_pos)
        mov.stop()
        
    elif keys[Key.up]:
        print('key up is working')
        mov.forward()
        mov.stop()

    elif keys[Key.down]:
        print('key down is working')
        mov.reverse()
        mov.stop()
        
    elif keys[Key.left]:
        print('key left is working')
        servo_pos +=5
        if servo_pos <= 130:
            mov.steer(servo_pos)
        if servo_pos > 130:
            mov.steer(130)
            servo_pos = 130
    
    elif keys[Key.right]:
        print('key right is working')
        servo_pos -=5
        if servo_pos >= 55 and servo_pos < 91:
            mov.steer(servo_pos)
        if servo_pos < 55:
            mov.steer(55)
            servo_pos = 55
    else:
        servo_pos = 90
        mov.steer(servo_pos)
        mov.stop()
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

