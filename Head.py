#!/bin/python
'''
This module holds Inmoov's head

Authors:
    - Brett Creeley
    - Matty Baba "Black Sheep" Allos
    - Dai Ho
'''
from Config import degrees_to_pulse, set_pwm
from HalfRotationServo import HalfRotationServo

class Head(object):
    '''
    This class is used to control the motion of Inmoov's head.
    - Todo: Add mouth and eye control.
    '''
    SERVO_MIN = 200   # Found from Calibrate_Servo.py -- part#: HS-805BB
    SERVO_MAX = 525   # Found from Calibrate_Servo.py -- part#: HS-805BB

    def __init__(self, x_channel, y_channel):
        '''
        Initialize all of Inmoov's head variables
        '''

        # Setup x-axis Servo control on the specified channel
        self.x_channel = x_channel
        self.x_servo = HalfRotationServo(
            self.x_channel, self.SERVO_MIN, self.SERVO_MAX)

        # Setup y-axis Servo control on the specified channel
        self.y_channel = y_channel
        self.y_servo = HalfRotationServo(
            self.y_channel, self.SERVO_MIN, self.SERVO_MAX)

        # Start Head facing forward
        self.initialize()

    def initialize(self):
        '''
        Make head look straight forward x and y-axis
        '''
        self.x_servo.rotate(0)
        self.y_servo.rotate(0)

    def move_y(self, degrees):
        '''
        Move head to y-axis to the degree postion.
        - -90 degrees places Inmoov's chin to his chest.
        -   0 degrees makes Inmoov look forward.
        -  90 degrees makes Inmoov look up.
        '''
        self.y_servo.rotate(degrees)

    def move_x(self, degrees):
        '''
        Move head to x-axis to the degree postion.
        - -90 degrees moves Inmoov's head all the way right.
        -   0 degees makes Inmoov look forward.
        -  90 degrees moves Inmoov's head all the way left.
        '''
        self.x_servo.rotate(degrees)
