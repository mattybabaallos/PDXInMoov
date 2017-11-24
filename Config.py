#!/bin/python
"""
This module holds the global pwm variable and any utility functions

Authors:
    - Brett Creeley
    - Matty Baba "Black Sheep" Allos
    - Dai Ho
"""
from Adafruit_PWM_Servo_Driver import PWM

pwm = PWM(0x40)
pwm.setPWMFreq(50)

def set_pwm(channel, pulse_on, pulse_off):
    """ Set the pwm for the channel specified """
    pwm.setPWM(channel, pulse_on, pulse_off)
