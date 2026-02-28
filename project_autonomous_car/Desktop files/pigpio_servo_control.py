import pigpio
import math

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

pi = pigpio.pi()
if not pi.connected:
    exit()
while True:
    pi = pigpio.pi()
    angle = float(input('Please enter a angle: '))
    pw = angleToPulseWidth(angle)
    print(pw)
    pi.set_servo_pulsewidth(GPIO_SERVO_PIN, pw)

# add or subtract 25 to 65 and 115 for full turn
# 65 = 50max 115 = 130
