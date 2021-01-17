#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Int32

rospy.init_node('rand')
pub = rospy.Publisher('rand', Int32, queue_size = 1)
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    n = random.randint(0, 200)
    pub.publish(n)
    rate.sleep()
