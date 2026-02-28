# Check this out - https://www.pygame.org/docs/ref/joystick.html
# Read it then use JOYAXISMOTION to get position of joystick
#  JOYBUTTONDOWN does not mean you're pressing the down position,
# but more like a button has been pressed.
# JOYBUTTONUP means a button got released (your thumb has let go of a button).
# This returns axis - pygame.joystick.Joystick.get_axis(axis_number)
# But you must have a joystick variable already set before using it.
# Why are you giving it axis_number when it is to return a axis
# Because your controller doesn't have just one axe, it might have two
# (because there are two thumb sticks).
# [0, 1] can mean the stick is at a 90 degree angle from the top origin clockwise

import os
import pygame

class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    def init(self):
        """Initialize the joystick components"""

        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def listen(self):
        """Listen for events to happen"""

        if not self.axis_data:
            self.axis_data = {}

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controller.get_numhats()):
                self.hat_data[i] = (0, 0)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    self.axis_data[event.axis] = round(event.value,2)
                elif event.type == pygame.JOYBUTTONDOWN:
                    self.button_data[event.button] = True
                elif event.type == pygame.JOYBUTTONUP:
                    self.button_data[event.button] = False
                elif event.type == pygame.JOYHATMOTION:
                    self.hat_data[event.hat] = event.value

                # Insert your code on what you would like to happen for each event here!dfddd.d.d.dd..d.............d.dddddd.d..ddd;..;;;;;k
                # In the current setup, I have the state simply printing out to the screen.
                def get_angle(Xaxis,Yaxis):
                    #To avoid ZeroDivisionError
                    #P.S. - you can improve it a bit.
                    if Xaxis == 0:
                        Xaxis = 0.001
                    if Yaxis == 0:
                        Yaxis = 0.001
                    #defining the third side of a triangle using the Pythagorean theorem
                    b = ((Xaxis)**2 + (Yaxis)**2)**0.5
                    c = Xaxis
                    a = Yaxis
                    #Using law of cosines we'll find angle using arccos of cos
                    #math.acos returns angles in radians, so we need to multiply it by 180/math.pi
                    angle =  math.acos((b**2 + c**2 - a**2) / (2*b*c)) * 180/math.pi
                    #It'll fix angles to be in range of 0 to 360
                    if Yaxis > 0:
                        angle = 360 - angle
                    return angle
                print(get_angle(event.value))
                os.system('clear')


if __name__ == "__main__":
    ps4 = PS4Controller()
    ps4.init()
    ps4.listen()
