#!/bin/python
'''
This module holds Inmoov's Torso

Authors:
    - Brett Creeley
    - Matty Baba "Black Sheep" Allos
    - Dai Ho
'''
from Config import degrees_to_pulse, set_pwm

class Torso(object):
    '''
    This class is used to control Inmoov's Torso.
    '''
    MIN_DEGREE = -90  # Found from Calibrate_Servo.py -- part#: HS-805BB
    MAX_DEGREE = 90   # Found from Calibrate_Servo.py -- part#: HS-805BB
    SERVO_MIN = 200   # Found from Calibrate_Servo.py -- part#: HS-805BB
    SERVO_MAX = 525   # Found from Calibrate_Servo.py -- part#: HS-805BB

    def __init__(self, l_channel, r_channel):
        '''
        Initialize all of Inmoov's Torso variables.
        '''
        self.l_channel = l_channel    # Pi hat channel that the left servo is connected to
        self.r_channel = r_channel    # Pi hat channel that the right servo is connected to
        self.initialize()

    def initialize(self):
        '''
        Center Inmoov's Torso.
        '''
        self.lean(90)

    def lean(self, degrees):
        '''
        Make Inmoov lean based on the specified degree.
        - -90 degrees leans Inmoov all the way right.
        -   0 degrees centers Invmoov's Torso.
        -  90 degrees leans Inmoov all the way left.
        '''
        pulse = degrees_to_pulse(degrees, self.MIN_DEGREE, s0lf.MAX_DEGREE,
                                 self.SERVO_MIN, self.SERVO_MAX)
        set_pwm(self.l_channel, 0, pulse)
        set_pwm(self.r_channel, 0, pulse)
