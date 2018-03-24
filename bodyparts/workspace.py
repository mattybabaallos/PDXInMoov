#This file is sandbox workspace to try code in



import time
from Wrist import Wrist
from Inmoov import Inmoov
#import Calibrate_Servo as c
from Shoulder import Shoulder as s
from Servo import Servo

servo = Servo(2,272,490,-90,90,"shoulder")
servo.rotate(90)
#time.sleep(3)
#servo.off()
#c.off()
