#!/bin/python
from Adafruit_PWM_Servo_Driver import PWM
import time
import Calibration_Servo

# Left/Right Torso - HS-805BB
servoMin = Calibration_Servo.determineServoPulse(800, 50)
servoMax = Calibration_Servo.determineServoPulse(2100, 50)
servoMid = Calibration_Servo.determineServoPulse(1500, 50)
servo135 = Calibration_Servo.determineServoPulse(1900, 50)

pwm = PWM(0x40)
pwm.setPWMFreq(50)

print "ServoMin = ", servoMin
print "ServoMax = ", servoMax



def headUp():
    pwm.setPWM(2, 0, servoMax)

def headDown():
    pwm.setPWM(2, 0, servoMin)

def headMid():
    pwm.setPWM(2, 0, servoMid)

def leanLeft():
    pwm.setPWM(0, 0, servoMax)
    pwm.setPWM(1, 0, servoMax)

def leanRight():
    pwm.setPWM(0, 0, servoMin)
    pwm.setPWM(1, 0, servoMin)

def leanCenter():
    pwm.setPWM(0, 0, servoMid)
    pwm.setPWM(1, 0, servoMid)

def initialize():
    headMid()
    leanCenter()

initialize()
time.sleep(1)
headUp()
leanLeft()
time.sleep(1)
headDown()
leanRight()
time.sleep(2)
headMid()
leanCenter()

