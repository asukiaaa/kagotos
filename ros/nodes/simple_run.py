#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

def set_motor_speed(left, right):
    twist = Twist()
    if (left > 0.0 and right > 0.0):
        twist.linear.x = 1.0
    elif (left <= 0.0 and right > 0.0):
        # Turn left
        twist.angular.z = 1.0
        if (left == 0.0):
            twist.linear.x = 1.0
    elif (left > 0.0 and right <= 0.0):
        # Turn right
        twist.angular.z = -1.0
        if (right == 0.0):
            twist.linear.x = 1.0
    elif (left < 0.0 and right < 0.0):
        twist.linear.x = -1.0
    pub.publish(twist)

def laser_scan_callback(data):
    print "get laser info"
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    # print data.ranges
    print len(data.ranges)
    min_range = 10
    for range in data.ranges[270:450]:
        # print range
        if range != 0.0 and range < min_range:
            min_range = range
    if min_range < 0.4:
        set_motor_speed(100, -100)
    elif min_range < 0.6:
        set_motor_speed(100, 0)
    else:
        set_motor_speed(100, 100)

if __name__ == '__main__':
    rospy.init_node('sample_listener')
    rospy.Subscriber("/scan", LaserScan, laser_scan_callback)
    print "set subscriber"
    rospy.spin()
