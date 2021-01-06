#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def cb(message):
    num = message.data

    t = 0
    for i in range(1, num):
        if num % i == 0:
            t+=1
    if t == 1:
        print(num)

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb)
    rospy.spin()
