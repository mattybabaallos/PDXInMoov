#!/bin/python
'''
This module holds Inmoov's head

Authors:
    - Brett Creeley
    - Matty Baba "Black Sheep" Allos
    - Dai Ho
'''
from Config import degrees_to_pulse, set_pwm

class Head(object):
    '''
    This class is used to control the motion of Inmoov's head.
    - Todo: Add mouth and eye control.
    '''
    MIN_DEGREE = 0    # Found from Calibrate_Servo.py -- part#: HS-805BB
    MAX_DEGREE = 180  # Found from Calibrate_Servo.py -- part#: HS-805BB
    SERVO_MIN = 200   # Found from Calibrate_Servo.py -- part#: HS-805BB
    SERVO_MAX = 525   # Found from Calibrate_Servo.py -- part#: HS-805BB

    def __init__(self, x_channel, y_channel):
        '''
        Initialize all of Inmoov's head variables
        '''
        self.x_channel = x_channel    # Pi hat channel that the x-axis servo is connected to
        self.y_channel = y_channel    # Pi hat channel that the y-axis servo is connected to
        self.initialize()

    def initialize(self):
        '''
        Make head look straight forward x and y-axis
        '''
        self.move_y(90)
        self.move_x(90)

    def move_y(self, degrees):
        '''
        Move head to y-axis to the degree postion.
        - 0 degrees places Inmoov's chin to his chest.
        - 90 degrees makes Inmoov look forward.
        - 180 degrees makes Inmoov look up.
        '''
        pulse = degrees_to_pulse(degrees, self.MIN_DEGREE, self.MAX_DEGREE,
                                 self.SERVO_MIN, self.SERVO_MAX)
        set_pwm(self.y_channel, 0, pulse)

    def move_x(self, degrees):
        '''
        Move head to x-axis to the degree postion.
        - 0 degrees moves Inmoov's head all the way right.
        - 90 degees makes Inmoov look forward.
        - 180 degrees moves Inmoov's head all the way left.
        '''
        pulse = degrees_to_pulse(degrees, self.MIN_DEGREE, self.MAX_DEGREE,
                                 self.SERVO_MIN, self.SERVO_MAX)
        set_pwm(self.x_channel, 0, pulse)
