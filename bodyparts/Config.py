#!/bin/python
"""
This module holds the global pwm variable and any utility functions

Authors:
    Brett Creeley
    Matty Baba Allos
"""
from Adafruit_PWM_Servo_Driver import PWM

pwm_shield_0 = PWM(0x40)
#pwm_shield_1 = PWM(0x41)
#pwm_shield_2 = PWM(0x42)
pwm_shield_0.setPWMFreq(50)

# Can only have 16 channels per Adafruit PWM Pi Hat
MIN_CHANNEL = 0
MAX_CHANNEL = 15


def set_pwm(shield_id, channel, pulse_on, pulse_off):
    """ Set the pwm for the channel specified """
    
    """ Don't allow invalid channel values """
    if channel > MAX_CHANNEL or channel < MIN_CHANNEL :
        raise ValueError('Channel must be between 0 and 15 inclusive')

    if shield_id == 0:
        pwm_shield_0.setPWM(channel, pulse_on, pulse_off)
    elif shield_id == 1:
        raise ValueError("Unimplemented shield_id {}".format(shield_id))
    elif shield_id == 2:
        raise ValueError("Unimplemented shield_id {}".format(shield_id))
    else:
        raise ValueError("Invalid shield_id")

