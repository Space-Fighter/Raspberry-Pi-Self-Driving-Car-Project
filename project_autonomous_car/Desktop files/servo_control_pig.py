import time
 
import pigpio
 
servos = 10 #GPIO number
 
pi = pigpio.pi()

#pulsewidth can only set between 500-2500
try:
    while True:
 
        pi.set_servo_pulsewidth(servos, 500) #0 degree
        print("Servo {} {} micro pulses".format(servos, 1000))
        time.sleep(1)
        pi.set_servo_pulsewidth(servos, 1500) #90 degree
        print("Servo {} {} micro pulses".format(servos, 1500))
        time.sleep(1)
        pi.set_servo_pulsewidth(servos, 2500) #180 degree
        print("Servo {} {} micro pulses".format(servos, 2000))
        time.sleep(1)
        pi.set_servo_pulsewidth(servos, 1500)
        print("Servo {} {} micro pulses".format(servos, 1500))
        time.sleep(1)
 
   # switch all servos off
except KeyboardInterrupt:
    pigpio.set_servo_pulsewidth(servos, 0);
 
pigpio.stop()
