#!/bin/python
"""
This module contains an Inmoov Forearm

Authors:
    Brett Creeley
    Matty Baba Allos
"""

class Forearm(object):
    """
    This class represents an Inmoov Forearm
    """

    def __init__(self, hand, wrist):
        """
        Build an Inmoov Forearm
        """
        if hand is None or wrist is None
            raise "Could not build a forearm"
        self.wrist = wrist
        self.hand = hand

    def off(self):
        self.wrist.off()
        self.hand.off()