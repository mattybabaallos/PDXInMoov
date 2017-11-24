#!/bin/python
"""
This module are Inmoov!

Authors:
    - Brett Creeley
    - Matty Baba "Black Sheep" Allos
    - Dai Ho
"""
from Head import Head
from Torso import Torso
from Forearm import Forearm

class Inmoov(object):
    """
    This class are Inmoov!
    """
    HEAD_X_CHANNEL  = 0
    HEAD_Y_CHANNEL  = 1
    TORSO_L_CHANNEL = 2
    TORSO_R_CHANNEL = 3
    L_WRIST_CHANNEL = 4
    R_WRIST_CHANNEL = 5
    L_PINKY_FINGER_CHANNEL = 6
    L_RING_FINGER_CHANNEL  = 7
    L_MID_FINGER_CHANNEL   = 8
    L_INDEX_FINGER_CHANNEL = 9
    L_THUMB_CHANNEL        = 10
    R_PINKY_FINGER_CHANNEL = 11
    R_RING_FINGER_CHANNEL  = 12
    R_MID_FINGER_CHANNEL   = 13
    R_INDEX_FINGER_CHANNEL = 14
    R_THUMB_CHANNEL        = 15


    def __init__(self):
        """
        Build all of Inmoov's parts.
        """
        self.head = Head(self.HEAD_X_CHANNEL, self.HEAD_Y_CHANNEL)
        self.torso = Torso(self.TORSO_L_CHANNEL, self.TORSO_R_CHANNEL)
        """
        Todo: Move the Forearm objects into the Arm class (unimplemented)
        """
        self.left_forearm = Forearm(self.L_PINKY_FINGER_CHANNEL,
                                    self.L_RING_FINGER_CHANNEL,
                                    self.L_MID_FINGER_CHANNEL,
                                    self.L_INDEX_FINGER_CHANNEL,
                                    self.L_THUMB_CHANNEL,
                                    self.L_WRIST_CHANNEL)
        self.right_forearm = Forearm(self.R_PINKY_FINGER_CHANNEL,
                                     self.R_RING_FINGER_CHANNEL,
                                     self.R_MID_FINGER_CHANNEL,
                                     self.R_INDEX_FINGER_CHANNEL,
                                     self.R_THUMB_CHANNEL,
                                     self.R_WRIST_CHANNEL)
