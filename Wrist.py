#!/bin/python
"""
This module holds an Inmoov wrist

Authors:
    Brett Creeley
    Matty Baba "Black Sheep" Allos
    Dai Ho
"""
from Servo import Servo


class Wrist(object):
    """ This class represents an Inmoov Wrist """

    """
    Todo: Pull apart Inmoov's forearm to find out servo models for a Wrist.
        - These values are just copied from the HS-805BB Servo.
    """

    SERVO_MIN = 200   # Found from Calibrate_Servo.py -- part#: Todo: Find
    SERVO_MAX = 525   # Found from Calibrate_Servo.py -- part#: Todo: Find

    def __init__(self, channel):
        """ Set the Servo for this Wrist """
        try:
            self.servo = Servo(channel, self.SERVO_MIN, self.SERVO_MAX)
        except ValueError:
            print("Could not initiate wrist on channel", channel)

    def rotate(self, degree):
        """ Rotate this Wrist the desired degree """
        self.servo.rotate(degree)

    def off(self):
        """ Turn off all fingers off"""
        self.servo.off()
