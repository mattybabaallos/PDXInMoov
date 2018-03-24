#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16

def send_body():
    rospy.init_node('brain', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    pub = rospy.Publisher('brain', Int16, queue_size=10)
    while not rospy.is_shutdown():
        pub.publish(1)
        rate.sleep()

if __name__ == '__main__':
    try:
        send_body()
    except rospy.ROSInterruptException:
        pass
