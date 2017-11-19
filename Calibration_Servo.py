#!/bin/python

# Returns servo pulse how the library wants it based
# on the input being a datasheet value
def determineServoPulse(pulse_max_ds, hz):
    micro_per_sec = 1000000
    period =  micro_per_sec / hz
    time_per_tick = period / 4096 # 12-bit resolution
    return pulse_max_ds / time_per_tick

