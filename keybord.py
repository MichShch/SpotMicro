#!/usr/bin/python

import rospy
from std_msgs.msg import Bool, Int8

msg = """
Spot Micro Walk Command

Enter one of the following options:
-----------------------------
quit: stop and quit the program
walk: Start walk mode and keyboard motion control
stand: Stand robot up
idle: Lay robot down
sit: Sit robot

Keyboard commands for body motion 
---------------------------
   q   w   e            u
   a   s   d    
            

  u: Quit body motion
  w: Forward step
  a: Left step
  s: Backward step
  d: Right step
  q: Rate left
  e: Rate right

  anything else : Prompt again for command

CTRL-C to quit
"""

valid_cmds = ('quit', 'walk', 'stand', 'idle', 'sit')

_ros_pub_walk_cmd = rospy.Publisher('/walk_cmd', Bool, queue_size=1)
_ros_pub_walk_x_cmd       = rospy.Publisher('/walk_x_cmd',Int8, queue_size=1)
_ros_pub_walk_y_cmd       = rospy.Publisher('/walk_y_cmd',Int8, queue_size=1)
_ros_pub_angle_cmd = rospy.Publisher('/angle_cmd', Int8, queue_size=1)
_ros_pub_stand_cmd      = rospy.Publisher('/stand_cmd',Bool,queue_size=1)
_ros_pub_idle_cmd       = rospy.Publisher('/idle_cmd',Bool,queue_size=1)
_ros_pub_sit_cmd       = rospy.Publisher('/sit_cmd',Bool,queue_size=1)

rospy.loginfo("Keyboard control node start complete")

while not rospy.is_shutdown():
    print(msg)
    userInput = input("Command?: ")
    if userInput not in valid_cmds:
        rospy.logwarn('Invalid keyboard command entered: %s', userInput)
    else:
        if userInput == 'quit':
            rospy.loginfo("Exiting...")
            break

        elif userInput == 'stand':
            _ros_pub_stand_cmd.publish(True)
            rospy.loginfo('Stand.')

        elif userInput == 'idle':
            _ros_pub_idle_cmd.publish(True)
            rospy.loginfo('Idle.')
        elif userInput == 'sit':
            _ros_pub_sit_cmd.publish(True)
            rospy.loginfo('Sit.')
        elif userInput == 'walk':
            _ros_pub_walk_cmd.publish(True)
            rospy.loginfo('walk.')
            while (1):
                userInput = input()

                if userInput == 'u':
                    _ros_pub_stand_cmd.publish(True)
                    rospy.loginfo('Quit.')
                    break

                elif userInput not in ('w', 'a', 's', 'd', 'q', 'e', 'u', 'f'):
                    print('Invalid comand')
                    rospy.logwarn('Invalid keyboard command : %s', userInput)
                else:
                    if userInput == 'w':
                        _ros_pub_vel_cmd.publish(1)

                    elif userInput == 's':
                        _ros_pub_vel_cmd.publish(-1)

                    elif userInput == 'a':
                        _ros_pub_vel_cmd.publish(-1)

                    elif userInput == 'd':
                        _ros_pub_vel_cmd.publish(1)

                    elif userInput == 'q':
                        _ros_pub_vel_cmd.publish(1)

                    elif userInput == 'e':
                        _ros_pub_vel_cmd.publish(-1)
