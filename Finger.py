#!/bin/python
"""
This module holds an Inmoov Finger.

Authors:
    Brett Creeley
    Matty Baba Allos
"""
from Servo import Servo

class Finger(object):
    """
    This class represents an Inmoov Finger.
    """

    """
    Todo: Pull apart Inmoov's forearm to find out servo models for fingers.
        - These values are just copied from the HS-805BB Servo.
    """
    SERVO_MIN = 200   # Found from Calibrate_Servo.py -- part#: Todo: Find
    SERVO_MAX = 525   # Found from Calibrate_Servo.py -- part#: Todo: Find

    def __init__(self, servo):
        
        if servo is None:
            raise Exception("Could not initialize Finger")
        
        self.servo = servo

    def bend_max(self):
        """
        Bend the Finger the max amount
        - Todo: Determine whether this needs to be 90 or -90
        """
        self.servo.rotate(-90)

    def bend(self, degree):
        """
        Bend the Finger
        """
        self.servo.rotate(degree)

    def straighten_max(self):
        """
        This is to make the finger straight.
        - Todo: Determine whether this needs to be 90 or -90
        """
        self.servo.rotate(90)

    def off(self):
        self.servo.off()
