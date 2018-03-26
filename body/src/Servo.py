#!/bin/bash

"""
Authors:
    Brett Creeley
    Matty Baba Allos
"""
from Config import set_pwm
import warnings

class Servo(object):
    """
    Servo stores the following values:
        channel: The channel the Servo is connected to
        min_pulse: The minimum pulse the Servo allows
        max_pulse: The maximum pulse the Servo allows
        min_degree: The minimum degree the Servo can rotate to
        max_degree: The maximum degree the Servo can rotate to
        default_angle: The rest(initial)position of the servo.
        name: The name of the servo
    """

    def __init__(self,
         id,
         min_pulse,
         max_pulse,
         min_degree=None,
         max_degree=None,
         default_angle= None,
         name="servo"
         ):
        self.id = id
        self.channel = self._id_to_channel(id)
        self.shield_id = self._id_to_shield_id(id)
        self.min_pulse = min_pulse
        self.max_pulse = max_pulse
        self.min_degree = min_degree
        self.max_degree = max_degree
        self.default_angle = default_angle
        self.name = name

    def _id_to_channel(self,id):
        """Given the id of the servo starting from 0 and because there
        are only 16 channels on hat we can know which channel the servo
        is connected into if we take the mod of the id. For example,
        a servo with id 34 is connected to channel 2 because 34%16 gives
        2 because 16 fits into 34 two times and we left 2"""
        return id % 16

    def _id_to_shield_id(self,id):
        """Given the id of the servo starting from 0 and because there
        are only 16 channels on hat we can know which shield the servo is plugged into
        if we divide the id by 16 and rounding to nearest integer.
        for example if we have servo plugged into channel 33
        we know it's on shield 2, counting from 0, because 33/16=2.06
        we round to the nearest int and we get a 2"""
        return int(round(id / 16)) #Make sure it's an int

    def rotate(self, degree):
        """ Rotate to the specified degrees """
        try:
            pulse = self.degrees_to_pulse(degree)
            print "current pulse", pulse
            set_pwm(self.shield_id,self.channel, 0, pulse)
        except ValueError as exception:
            print(exception)
            print("Could not rotate {} to {} degree").format(self.name, degree)

    def initialize(self):
        """ Move servo to defult position """
        self.rotate(self.default_angle)

    def off(self):
        """ Rotate to the specified degrees """
        try:
            set_pwm(self.shield_id,self.channel, 0, 0)
        except ValueError as exception:
            print(exception)
            print("Could not turn off {}").format(self.name)

    def degrees_to_pulse(self, degree):
        """ Map degree input value to a pulse length output value """
        pulse = ((degree - self.min_degree)
                 * (self.max_pulse - self.min_pulse + 1)
                 / (self.max_degree - self.min_degree + 1)
                 + self.min_pulse)

        # Check for boundary values
        if pulse < self.min_pulse:
            warnings.warn("Degree is out of range")
            return self.min_pulse
        elif pulse > self.max_pulse:
            warnings.warn("Degree is out of range")
            return self.max_pulse
        else:
            return pulse

    @property
    def min_pulse(self):
        return self.min_pulse

    @min_pulse.setter
    def min_pulse(self, value):
        """ Don't allow negative min_pulse value """
        if value >= 0:
            self.min_pulse = value
        else:
            raise ValueError('Servo min_pulse must be >= 0')

    @min_pulse.getter
    def min_pulse(self):
        return self.min_pulse

    @property
    def max_pulse(self):
        return self.max_pulse

    @max_pulse.setter
    def max_pulse(self, value):
        """ Don't allow negative/zero max_pulse value """
        if value > 0:
            self.max_pulse = value
        else:
            raise ValueError('Servo max_pulse must be > 0')

    @max_pulse.getter
    def max_pulse(self):
        return self.max_pulse

    @property
    def min_degree(self):
        return self.min_degree

    @min_degree.setter
    def min_degree(self, value=None):
        """ Only allow degree between -360 and 360 """
        if value is None:
            # Default value
            self.min_degree = -90
        elif value >= -360 and value <= 360:
            self.min_degree = value
        else:
            raise ValueError(
                'Servo min_degree must be between -360 and 360 inclusive')

    @min_degree.getter
    def min_degree(self):
        return self.min_degree

    @property
    def max_degree(self):
        return self.max_degree

    @max_degree.setter
    def max_degree(self, value=None):
        """ Only allow degree between -360 and 360 """

        if value is None:
            # Default value
            self.max_degree = 90
        elif value >= -360 and value <= 360:
            self.max_degree = value
        else:
            raise ValueError(
                'Servo max_degree must be between -360 and 360 inclusive')

    @max_degree.getter
    def max_degree(self):
        return self.max_degree

    @property
    def default_angle(self):
        return self.default_angle

    @default_angle.getter
    def default_angle(self):
        return self.default_angle
