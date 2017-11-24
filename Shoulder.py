#!/bin/python
"""
This module contains an Inmoov Shoulder

Authors:
    Brett Creeley
    Matty Baba "Black Sheep" Allos
    Dai Ho
"""
from Servo import Servo


class Shoulder(object):
    """ This class represents an Inmoov Shoulder """

    SERVO_MIN = 200   # Found from Calibrate_Servo.py -- part#: Todo: Find
    SERVO_MAX = 525   # Found from Calibrate_Servo.py -- part#: Todo: Find

    def __init__(self, flexion_channel, abduction_channel, rotation_channel):
        """ Build an Inmoov Shoulder """
        try:
            self.flexion_servo = Servo(
                flexion_channel, self.SERVO_MIN, self.SERVO_MAX)
            self.abduction_servo = Servo(
                abduction_channel, self.SERVO_MIN, self.SERVO_MAX)
            self.rotation_servo = Servo(
                rotation_channel, self.SERVO_MIN, self.SERVO_MAX)
        except ValueError:
            print("Could not initiate shoulder on channel")

    def initialize(self):
        """
        Make the arm in down postion
        """
        self.flexion_servo.rotate(0)
        self.abduction_servo.rotate(0)
        self.rotation_servo.rotate(0)

    def flex(self, degree):
        """TODO maybe check degrees """
        self.flexion_servo.rotate(degree)

    def extend(self, degree):
        self.flexion_servo.rotate(degree)

    def abduction_up(self, degree):
        self.abduction_servo.rotate(degree)

    def abduction_down(self, degree):
        self.abduction_servo.rotate(degree)

    def rotation_internal(self, degree):
        self.rotation_servo.rotate(degree)

    def rotation_external(self, degree):
        self.rotation_servo.rotate(degree)

    def off(self):
        self.rotation_servo.off()
        self.abduction_servo.off()
        self.flexion_servo.off()
