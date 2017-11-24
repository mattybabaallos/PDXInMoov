#!/bin/python
"""
This module holds Inmoov's Torso

Authors:
    - Brett Creeley
    - Matty Baba "Black Sheep" Allos
    - Dai Ho
"""
from Servo import Servo


class Torso(object):
    """ This class is used to control Inmoov's Torso """
    SERVO_MIN = 200   # Found from Calibrate_Servo.py -- part#: HS-805BB
    SERVO_MAX = 525   # Found from Calibrate_Servo.py -- part#: HS-805BB

    def __init__(self, l_channel, r_channel):
        """
        Initialize all of Inmoov's Torso variables.
        """
        try:
            self.l_servo = Servo(l_channel, self.SERVO_MIN, self.SERVO_MAX)
            self.r_servo = Servo(r_channel, self.SERVO_MIN, self.SERVO_MAX)
            self.lean(0)  # Make Torso straight
        except ValueError:
            print("Could not initialize Torso on channels", l_channel, r_channel)

    def initialize(self):
        self.lean(0)

    def lean(self, degrees):
        """
        Make Inmoov lean based on the specified degree.
        - -90 degrees leans Inmoov all the way right.
        -   0 degrees centers Invmoov's Torso.
        -  90 degrees leans Inmoov all the way left.
        """
        self.l_servo.rotate(degrees)
        self.r_servo.rotate(degrees)

    def off(self):
        """ Turn off all fingers off"""
        self.l_servo.off()
        self.r_servo.off()
