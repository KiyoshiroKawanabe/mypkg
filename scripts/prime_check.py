#!/usr/bin/env python3
import rospy
import RPi.GPIO as GPIO
import time, sys
from std_msgs.msg import Int32

red_led = 2
green_led = 5

GPIO.setmode(GPIO.BCM)

GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

def cb(message):
    num = message.data

    t = 0
    for i in range(1, num):
        if num % i == 0:
        t+=1
    
    if t == 1:
        print(num,'\tは素数です')
        GPIO.output(red_led, 1)
        GPIO.output(green_led, 0)
    else:
        print(num,'\tは違います')
        GPIO.output(red_led, 0)
        GPIO.output(green_led, 1)

    if __name__ == '__main__':
        rospy.init_node('led')
        sub = rospy.Subscriber('rand', Int32, cb)
        rospy.spin()
