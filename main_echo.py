#!/usr/bin/python
import rospy
from std_msgs.msg import Int8, Bool
def walk(data):
    rospy.loginfo("walk mode",data.data)
    rospy.Subscriber('/walk_x_cmd', Int8, step_x)
    rospy.Subscriber('/walk_y_cmd', Int8, step_y)
    rospy.Subscriber('/angle_cmd', Int8, angle)
    rospy.Subscriber('/stand_cmd', Bool, lisener)
    rospy.spin()

def step_x(data):
    rospy.loginfo("step x", data.data)

def step_y(data):
    rospy.loginfo("step y", data.data)

def angle(data):
    rospy.loginfo("angle", data.data)

def stand(data):
    rospy.loginfo("stand mode", data.data)

def idle(data):
    rospy.loginfo("idle mode", data.data)

def sit(data):
    rospy.loginfo("sit mode", data.data)

def lisener():
    rospy.Subscriber('/walk_cmd', Bool, walk)
    rospy.Subscriber('/stand_cmd', Bool, walk)
    rospy.Subscriber('/idle_cmd', Bool, walk)
    rospy.Subscriber('/sit_cmd', Bool, walk)
    rospy.spin()