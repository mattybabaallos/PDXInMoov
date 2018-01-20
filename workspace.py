#This file is sandbox workspace to try code in


import json
from Servo import Servo
import time
from Wrist import Wrist
from Inmoov import Inmoov


inmo = Inmoov()
inmo.head.move_x(90)
time.sleep(0.5)
inmo.head.off()


