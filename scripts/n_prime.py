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
    print(num,'\tは素数です')
  else:
    print(num,'\tは違います')

if __name__ == '__main__':
  rospy.init_node('prime')
  sub = rospy.Subscriber('rand', Int32, cb)
  rospy.spin()
