#!/bin/python
'''
This module holds an Inmoov wrist

Authors:
    Brett Creeley
    Matty Baba "Black Sheep" Allos
    Dai Ho
'''
from Config import set_pwm, degrees_to_pulse

class Wrist(object):
    '''
    This class represents an Inmoov Wrist
    '''

    '''
    Todo: Pull apart Inmoov's forearm to find out servo models for a Wrist.
        - These values are just copied from the HS-805BB Servo.
    '''
    MIN_DEGREE = -90  # Found from Calibrate_Servo.py -- part#: Todo: Find
    MAX_DEGREE = 90   # Found from Calibrate_Servo.py -- part#: Todo: Find
    SERVO_MIN = 200   # Found from Calibrate_Servo.py -- part#: Todo: Find
    SERVO_MAX = 525   # Found from Calibrate_Servo.py -- part#: Todo: Find

    def __init__(self, channel):
        '''
        Set the channel for this Wrist.
        '''
        self.channel = channel

    def rotate(self, degrees):
        '''
        Rotate this Wrist the desired degrees.
        '''
        pulse = degrees_to_pulse(degrees, self.MIN_DEGREE, self.MAX_DEGREE,
                                 self.SERVO_MIN, self.SERVO_MAX)
        set_pwm(self.channel, 0, pulse)
