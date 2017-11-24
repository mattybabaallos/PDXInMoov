#!/bin/bash

from Config import degrees_to_pulse, set_pwm
class HalfRotationServo(object):
    """
    This represents a Servo that has the ability to rotate 180 degrees
    """
    MIN_DEGREE = -90
    MAX_DEGREE =  90

    def __init__(self, channel, min_pulse, max_pulse):
        self.min_pulse = min_pulse
        self.max_pulse = max_pulse
        self.channel = channel

    """
    Rotate to the specified degrees
    """
    def rotate(self, degrees):
        pulse = degrees_to_pulse(degrees, self.MIN_DEGREE, self.MAX_DEGREE,
                                 self.min_pulse, self.max_pulse)
        set_pwm(self.channel, 0, pulse)
