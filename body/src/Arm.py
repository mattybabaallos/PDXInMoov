#!/bin/python
"""
This module contains an Inmoov Arm

Authors:
    Brett Creeley
    Matty Baba Allos
"""


class Arm(object):
    """
    This class represents an Inmoov Arm
    """

    def __init__(self, forearm, shoulder):
        """
        Build an Inmoov Arm
        """
        if forearm is None or shoulder is None:
            raise "Could not build a arm"
        self.forearm = forearm
        self.shoulder = shoulder

    def off(self):
        self.forearm.off()
        self.shoulder.off()
