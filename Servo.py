#!/bin/bash

from Config import set_pwm
class Servo(object):
    """
    Servo stores the following values:
        channel: The channel the Servo is connected to
        min_pulse: The minimum pulse the Servo allows
        max_pulse: The maximum pulse the Servo allows
        min_degree: The minimum degree the Servo can rotate to
        max_degree: The maximum degree the Servo can rotate to
    """

    # Can only have 16 channels per Adafruit PWM Pi Hat
    MIN_CHANNEL = 0
    MAX_CHANNEL = 15

    def __init__(self, channel, min_pulse, max_pulse=None, min_degree=None,
                 max_degree=None):
        self.channel = channel
        self.min_pulse = min_pulse
        self.max_pulse = max_pulse
        self.min_degree = min_degree
        self.max_degree = max_degree

    def rotate(self, degree):
        """ Rotate to the specified degrees """
        try:
            pulse = self.degrees_to_pulse(degree)
            set_pwm(self._channel, 0, pulse)
        except ValueError:
            print("Could not rotate Servo to", degree)

    def degrees_to_pulse(self, degree):
        """ Map degree input value to a pulse length output value """
        if degree >= self.min_degree and degree <= self.max_degree:
            return ((degree - self.min_degree)
                    * (self.max_pulse - self.min_pulse + 1)
                    / (self.max_degree - self.min_degree + 1)
                    + self.min_pulse)
        else:
            raise ValueError("Invalid Servo input degree", degree)

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        """ Don't allow invalid channel values """
        if value >= self.MIN_CHANNEL and value <= self.MAX_CHANNEL:
            self._channel = value
        else:
            raise ValueError('Channel must be between 0 and 15 inclusive')

    @property
    def min_pulse(self):
        return self._min_pulse

    @min_pulse.setter
    def min_pulse(self, value):
        """ Don't allow negative min_pulse value """
        if value >= 0:
            self._min_pulse = value
        else:
            raise ValueError('Servo min_pulse must be >= 0')

    @min_pulse.getter
    def min_pulse(self):
        return self._min_pulse

    @property
    def max_pulse(self):
        return self._max_pulse

    @max_pulse.setter
    def max_pulse(self, value):
        """ Don't allow negative/zero max_pulse value """
        if value > 0:
            self._max_pulse = value
        else:
            raise ValueError('Servo max_pulse must be > 0')

    @max_pulse.getter
    def max_pulse(self):
        return self._max_pulse

    @property
    def min_degree(self):
        return self._min_degree

    @min_degree.setter
    def min_degree(self, value=None):
        """ Only allow degree between -360 and 360 """
        if value is None:
            self._min_degree = -90
        elif value >= -360 and value <= 360:
            self._min_degree = value
        else:
            raise ValueError(
                'Servo min_degree must be between -360 and 360 inclusive')

    @min_degree.getter
    def min_degree(self):
        return self._min_degree

    @property
    def max_degree(self):
        return self._max_degree

    @max_degree.setter
    def max_degree(self, value=None):
        """ Only allow degree between -360 and 360 """

        if value is None:
            self._max_degree = 90
        elif value >= -360 and value <= 360:
            self._max_degree = value
        else:
            raise ValueError(
                'Servo max_degree must be between -360 and 360 inclusive')

    @max_degree.getter
    def max_degree(self):
        return self._max_degree

