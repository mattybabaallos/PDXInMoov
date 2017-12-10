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

def set_pwm(shield_id, channel, pulse_on, pulse_off):
    """ Set the pwm for the channel specified """
    if shield_id == 0:
        pwm_shield_0.setPWM(channel, pulse_on, pulse_off)
    elif shield_id == 1:
        raise ValueError("Unimplemented shield_id", shield_id)
    elif shield_id == 2:
        raise ValueError("Unimplemented shield_id", shield_id)
    else:
        raise ValueError("Invalid shield_id", shield_id)

