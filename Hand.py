#!/bin/python
'''
This module holds an Inmoov Hand.

Authors:
    Brett Creeley
    Matty Baba "Black Sheep" Allos
    Dai Ho
'''
from Finger import Finger

class Hand(object):
    '''
    This class represents an Inmoov Hand.
    '''
    def __init__(self, pinky_channel, ring_channel, mid_channel, index_channel, thumb_channel):
        '''
        Build an Inmoov Hand
        '''
        self.pinky_finger = Finger(pinky_channel)
        self.ring_finger = Finger(ring_channel)
        self.mid_finger = Finger(mid_channel)
        self.index_finger = Finger(index_channel)
        self.thumb = Finger(thumb_channel)
        '''
        Todo: Initialize to some value
        '''

    def extend_all_fingers(self):
        '''
        Extend all fingers for waving/high-fiving/etc.
        '''
        self.pinky_finger.straighten()
        self.ring_finger.straighten()
        self.mid_finger.straighten()
        self.index_finger.straighten()
        self.thumb.straighten()

    def make_fist(self):
        '''
        Bend all fingers in to make a fist
        '''
        self.pinky_finger.bend_max()
        self.ring_finger.bend_max()
        self.mid_finger.bend_max()
        self.index_finger.bend_max()
        self.thumb.bend_max()

    def bend_fingers(self, pinky_deg=None, ring_deg=None, mid_deg=None,
                     index_deg=None, thumb_deg=None):
        '''
        Bend the Fingers that have values sent in.
        '''
        if pinky_deg is not None:
            self.pinky_finger.bend(pinky_deg)
        if ring_deg is not None:
            self.ring_finger.bend(ring_deg)
        if mid_deg is not None:
            self.mid_finger.bend(mid_deg)
        if index_deg is not None:
            self.index_finger.bend(index_deg)
        if thumb_deg is not None:
            self.thumb.bend(thumb_deg)
