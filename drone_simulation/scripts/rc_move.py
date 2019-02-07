#!/usr/bin/env python
# airsim
import setup_path
import airsim
# standard python
import math
import sys
import numpy as np
# ROS
import rospy
from sensor_msgs.msg import Joy

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)

def rc_callback(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.axes[1])
    client.moveByAngleThrottleAsync(-data.axes[1], -data.axes[0], -data.axes[5], -data.axes[3], 0.5 )

def airsim_rc():
    rospy.init_node('airsim_rc')
    rospy.Subscriber("/joy", Joy, rc_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        airsim_rc()
    except rospy.ROSInterruptException:
        pass