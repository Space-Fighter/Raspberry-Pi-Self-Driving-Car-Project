import picamera
import time
import cv2
import sys
import numpy as np
import movements as mov
import RPi.GPIO as gpio
import os
import tkinter as tk
import curses
signal = True

def key_input(event):
    mov.init()
    print('Key:', event.char)
    key_press = event.char
    gpio.setmode(gpio.BCM)
    gpio.setup(16, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    gpio.setup(25, gpio.OUT)
    output = [0, 0, 0, 0]
    try:
        while True:  
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                mov.forward()
            elif char == curses.KEY_DOWN:
                mov.reverse
            elif char == curses.KEY_RIGHT:
                mov.right
            elif char == curses.KEY_LEFT:
                mov.left()
    finally:
        #Close down curses properly, inc turn echo back on!
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        GPIO.cleanup()
        return output

file_name = 'training_data.npy'
if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, straiting fresh')
    while signal == True:
        screen = curses.initscr()
        curses.noecho() 
        curses.cbreak()
        screen.keypad(True)
def process_img(image):
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1 = 200, threshold2 = 300)
    return processed
##
##if key_press.lower() == 'w':
##        mov.forward()
##        output[0] = 1
##    elif key_press.lower() == 'a':
##        mov.left()
##        output[1] = 1
##    elif key_press.lower() == 's':
##        mov.reverse()
##        output[2] = 1
##    elif key_press.lower() == 'd':
##        mov.right()
##        output[3] = 1
##    elif key_press.lower() == 'e':
##        gpio.cleanup()
##        signal = False
##        return False
##    else:
##        gpio.cleanup()
