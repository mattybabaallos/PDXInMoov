#!/bin/python
'''
This module holds an Inmoov Finger.

Authors:
    Brett Creeley
    Matty Baba "Black Sheep" Allos
    Dai Ho
'''
from Config import set_pwm, degrees_to_pulse

class Finger(object):
    '''
    This class represents an Inmoov Finger.
    '''

    '''
    Todo: Pull apart Inmoov's forearm to find out servo models for fingers.
        - These values are just copied from the HS-805BB Servo.
    '''
    MIN_DEGREE = 0    # Found from Calibrate_Servo.py -- part#: Todo: Find
    MAX_DEGREE = 180  # Found from Calibrate_Servo.py -- part#: Todo: Find
    SERVO_MIN = 200   # Found from Calibrate_Servo.py -- part#: Todo: Find
    SERVO_MAX = 525   # Found from Calibrate_Servo.py -- part#: Todo: Find

    def __init__(self, channel):
        self.channel = channel

    def bend_max(self):
        '''
        Bend the Finger the max amount
        - Todo: Determine whether this needs to be SERVO_MAX or SERVO_MIN
        '''
        set_pwm(self.channel, 0, self.SERVO_MIN)

    def bend(self, degrees):
        '''
        Bend the Finger
        '''
        pulse = degrees_to_pulse(degrees, self.MIN_DEGREE, self.MAX_DEGREE,
                                 self.SERVO_MIN, self.SERVO_MAX)
        set_pwm(self.channel, 0, pulse)

    def straighten(self):
        '''
        This is to make the finger straight.
        - Todo: Determine whether this needs to be SERVO_MAX or SERVO_MIN
        '''
        set_pwm(self.channel, 0, self.SERVO_MAX)
