#!/bin/python
from Head import Head
from Torso import Torso

class Inmoov(object):
    '''
    This class are Inmoov!
    '''
    HEAD_X_CHANNEL = 0
    HEAD_Y_CHANNEL = 1
    TORSO_L_CHANNEL = 2
    TORSO_R_CHANNEL = 3

    def __init__(self):
        '''
        Build all of Inmoov's parts.
        '''
        self.head = Head(self.HEAD_X_CHANNEL, self.HEAD_Y_CHANNEL)
        self.torso = Torso(self.TORSO_L_CHANNEL, self.TORSO_R_CHANNEL)

    def move_head(self, x_degrees=None, y_degrees=None):
        '''
        Move Inmoov's head in the x and y-directions. If no x and/or
        y_degrees are specified then they are not used.
        '''
        if x_degrees is not None:
            self.move_head_x(x_degrees)
        if y_degrees is not None:
            self.move_head_y(y_degrees)

    def move_head_x(self, degrees):
        '''
        Move Inmoov's head in the x-direction.
        '''
        self.head.move_x(degrees)

    def move_head_y(self, degrees):
        '''
        Move Inmoov's head in the y-direction.
        '''
        self.head.move_y(degrees)

    def move_torso(self, degrees):
        '''
        Move Inmoov's torso.
        '''
        self.torso.lean(degrees)
