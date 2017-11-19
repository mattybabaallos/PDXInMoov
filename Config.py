#!/bin/python
'''
This module holds the global pwm variable and any utility functions

Authors:
    - Brett Creeley
    - Matty Baba "Black Sheep" Allos
    - Dai Ho
'''
from Adafruit_PWM_Servo_Driver import PWM

pwm = PWM(0x40)
pwm.setPWMFreq(50)

def set_pwm(channel, pulse_on, pulse_off):
    '''
    Set the pwm for the channel specified
    '''
    pwm.setPWM(channel, pulse_on, pulse_off)

def degrees_to_pulse(degree, min_degree, max_degree, min_pulse, max_pulse):
    '''
    Map x input value to output value
    '''
    if degree <= min_degree:
        return min_pulse
    elif degree >= max_degree:
        return max_pulse
    else:
        return ((degree - min_degree)
                * (max_pulse - min_pulse + 1) / (max_degree - min_degree + 1)
                + min_pulse)
