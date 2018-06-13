#!/usr/bin/env python
import serial
import rospy
from geometry_msgs.msg import Twist

ser = serial.Serial('/dev/ttyACM0')

def set_motor_speed(left, right):
    ser.write("motors {} {};".format(left, right))
    ser.flush()

def twist_callback(data):
    x = data.linear.x
    y = data.linear.y
    if (x == 0 and y == 0):
        set_motor_speed(0, 0);
    elif (x != 0):
        print "go or back"
        speed = 100 * x
        set_motor_speed(speed, speed)
    else:
        print "turn"
        speed = 50 * y
        set_motor_speed(speed, -speed)

if __name__ == '__main__':
    rospy.init_node('drive_base')
    rospy.Subscriber('/base_controller', Twist, twist_callback)
    rospy.spin()
