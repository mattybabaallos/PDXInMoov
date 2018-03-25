#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
from sensor_msgs.msg import CompressedImage


class brain:
   def __init__(self):
       self.pub = rospy.Publisher('brain', Int16, queue_size=10)
       self.subscriber = rospy.Subscriber("/raspicam_node/image/compressed", CompressedImage, self.callback,  queue_size =1)


   def callback(self,msg):
       rospy.loginfo("got an image")
       #call openCV work here
       self.pub.publish(1)
       #this is 1 is the motion ID InMoov will do

def main():
   rospy.init_node('brain', anonymous=True)
   b =brain()
   try:
       rospy.spin()
   except KeyboardInterrupt:
       rospy.loginfo("Inmoov brain is dead")

if __name__ == '__main__':
 main()

