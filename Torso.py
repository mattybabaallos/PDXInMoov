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

def headMidY():
    pwm.setPWM(2, 0, servoMid)

def headLeft():
    pwm.setPWM(3, 0, servoMax)

def headRight():
    pwm.setPWM(3, 0, servoMin)

def headMidX():
    pwm.setPWM(3, 0, servoMid-25)

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
    headMidX()
    headMidY()
    leanCenter()

initialize()
time.sleep(1)
headUp()
headLeft()
time.sleep(1)
leanLeft()
headRight()
time.sleep(1)
headMidX()
headDown()
leanRight()
time.sleep(1)
headMidY()
leanCenter()

