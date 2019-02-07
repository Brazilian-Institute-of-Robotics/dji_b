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
from drone_simulation.msg import position 

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
# drone takes off
client.takeoffAsync().join()

def move_callback(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.vel)
    client.moveToPositionAsync(data.x, data.y, data.z, data.vel).join()
    client.hoverAsync().join()

def airsim_move():
    rospy.init_node('airsim_move')
    rospy.Subscriber("/airsim_tests/go_to_goal", position, move_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        airsim_move()
    except rospy.ROSInterruptException:
        pass