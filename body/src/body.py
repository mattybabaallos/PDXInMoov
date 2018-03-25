#!/usr/bin/env python
import rospy

from std_msgs.msg import Int16
#from Inmoov import Inmoov
result = Int16()

def callback(msg):
    print("test")
    rospy.loginfo(msg.data)

def main():
    rospy.init_node("body")
    rospy.Subscriber("motion", Int16, callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
