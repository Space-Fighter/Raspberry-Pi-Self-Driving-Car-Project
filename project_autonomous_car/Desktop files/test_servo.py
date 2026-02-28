from time import sleep
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.OUT)
pwm = gpio.PWM(11,80)
pwm.start(0)

def SetAngle(angle):
    duty = angle / 18 + 2
    print(duty)
    gpio.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    gpio.output(11, False)
    # pwm.ChangeDutyCycle(0)
try:
    while True:
        angle = float(input('ENTER ANGLE PLEASE: '))
        SetAngle(angle)

except:
    SetAngle(0)
    pwm.stop()
    gpio.cleanup()
# 135 -right

# 65