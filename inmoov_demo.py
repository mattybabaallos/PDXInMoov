from Servo import Servo
from Torso import Torso
from Head import Head
import time


#torso = Torso(1, 0)
#torso.lean(-90)
#time.sleep(1.5)
#torso.lean(90)
#time.sleep(1.5)
#torso.lean(0)
#time.sleep(1.5)
#torso.off()

#arm = Servo(0, 2, 250, 500, -90, 90)
#arm.rotate(0)
#time.sleep(2)
#arm.rotate(-90)
#time.sleep(2)
#arm.off()

#elbow = Servo(0, 2, 125, 300, -90, 90)
#mouth = Servo(0, 11, 360, 450, -90, 90)
#elbow.rotate(-90)
#for i in range(0, 4, 1):
#    mouth.rotate(90)
#    time.sleep(0.5)
#    mouth.rotate(-90)
#    time.sleep(0.5)
#
#for i in range(0, 4, 1):
#    elbow.rotate(90)
#    time.sleep(1)
#    elbow.rotate(0)
#    time.sleep(1)
#
#elbow.rotate(-90)
#time.sleep(2)
#
#elbow.off()
#mouth.off()

#index = Servo(0, 8, 150, 500, -90, 90)
#ring = Servo(0, 5, 250, 575, 90, -90)
#thumb = Servo(0, 4, 225, 575, -90, 90)
#middle = Servo(0, 7, 150, 450, -90, 90)
#pinky = Servo(0, 3, 230, 420, -90, 90)
#
#for i in range(0, 2, 1):
#    index.rotate(-90)
#    ring.rotate(-90)
#    thumb.rotate(-90)
#    middle.rotate(-90)
#    pinky.rotate(-90)
#    time.sleep(1)
#    index.rotate(90)
#    ring.rotate(90)
#    thumb.rotate(90)
#    middle.rotate(90)
#    pinky.rotate(90)
#    time.sleep(1)

#index.off()
#ring.off()
#thumb.off()
#middle.off()
#pinky.off()



#mouth = Servo(0, 11, 360, 450, -90, 90)
#for i in range(0, 3, 1):
#    mouth.rotate(90)
#    time.sleep(1)
#    mouth.rotate(-90)
#    time.sleep(1)
#
#mouth.off()
#
head = Head(10, 9)
for i in range(0, 2, 1):
    head.move_x(-90)
    time.sleep(1)
    head.move_x(90)
    time.sleep(1)

head.move_x(0)
time.sleep(1)
head.off()

#time.sleep(2)
#head.move_y(-90)
#time.sleep(2)
#head.move_x(90)
#time.sleep(2)
#head.move_y(90)
#time.sleep(2)
#head.off()

#arm_flex = Servo(0, 12, 250, 500, -90, 90)
#arm_abduct = Servo(0, 13, 250, 500, -90, 90)
#arm_rotate = Servo(0, 14, 250, 600, -90, 90)


#arm_abduct.rotate(0)
#time.sleep(2)
#arm_flex.rotate(0)
#time.sleep(2)
#arm_rotate.rotate(-90)
#time.sleep(5)
#arm_rotate.rotate(90)
#time.sleep(5)
#arm_rotate.rotate(-90)
#time.sleep(5)


#arm_flex.off()
#arm_abduct.off()
#arm_rotate.off()