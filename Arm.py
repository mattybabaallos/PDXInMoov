#!/bin/python
"""
This module contains an Inmoov Arm

Authors:
    Brett Creeley
    Matty Baba "Black Sheep" Allos
    Dai Ho
"""
from Shoulder import Shoulder
from Forearm import Forearm


class Arm(object):
    """
    This class represents an Inmoov Arm
    """

    def __init__(self, pinky_channel, ring_channel, mid_channel,
                 index_channel, thumb_channel, wrist_channel,
                 flexion_channel, abduction_channel, rotation_channel):
        """
        Build an Inmoov Arm
        """
        self.forearm = Forearm(pinky_channel, ring_channel,
                               mid_channel, index_channel,
                               thumb_channel, wrist_channel)
        self.shoulder = Shoulder(flexion_channel,
                                 abduction_channel, rotation_channel)


   # def up(self)

    # def down(self)

    def off(self):
        self.forearm.off()
        self.shoulder.off()
