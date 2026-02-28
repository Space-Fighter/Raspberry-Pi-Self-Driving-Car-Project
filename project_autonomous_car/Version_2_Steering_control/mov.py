import RPi.GPIO as gpio
import pigpio
import math
import time
import tkinter as tk
import sys

def init():
    # To initialize pins
    gpio.setmode(gpio.BOARD)
    gpio.setup(3, gpio.OUT)
    gpio.setup(5, gpio.OUT)
    gpio.setup(7, gpio.OUT)
    gpio.setup(8, gpio.OUT)

init()

def forward():
    # 4 wheel drive(forward)
    gpio.output(3,  False)
    gpio.output(5, True)
    gpio.output(7, False)
    gpio.output(8, True)
    time.sleep(0.001)


def reverse():
    # 4 wheel drive(forward)
    gpio.output(3,  True)
    gpio.output(5, False)
    gpio.output(7, True)
    gpio.output(8, False)
    time.sleep(0.001)
pi = pigpio.pi()
if not pi.connected:
	exit()

def steer(angle):
	GPIO_SERVO_PIN  = 18
	MIN_ANG=-0 #degrees
	MAX_ANG=180.0  #degrees
	MIN_PW=1000 # microseconds
	MAX_PW=2000 # microseconds
	ANG_RANGE=MAX_ANG-MIN_ANG
	PW_RANGE=MAX_PW-MIN_PW
	PWAR=float(PW_RANGE)/ANG_RANGE
	RAD2DEG=180.0/math.pi
	def angleToPulseWidth(angle):
   		"""
   		angle is mapped to valid pulse widths for servo
  		which are determined by experiment.
  		"""
   		assert MIN_ANG <= angle <= MAX_ANG
   		return MIN_PW + ((angle - MIN_ANG) * PWAR)


	pw = angleToPulseWidth(angle)
	pi.set_servo_pulsewidth(GPIO_SERVO_PIN, pw)
