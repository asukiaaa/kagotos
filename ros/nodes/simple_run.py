#!/usr/bin/env python
import serial
import rospy
from sensor_msgs.msg import LaserScan

ser = serial.Serial('/dev/ttyACM0')
current_data = None

def update_direction():
    return

def set_motor_speed(left, right):
    ser.write("motors {} {};".format(left, right))
    ser.flush()

def laser_scan_callback(data):
    global current_data
    print "get laser info"
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    # print data.ranges
    print len(data.ranges)
    current_data = data
    min_range = 10
    for range in data.ranges[270:450]:
        # print range
        if range != 0.0 and range < min_range:
            min_range = range
    print min_range
    if min_range < 1:
        set_motor_speed(100, 0)
    else:
        set_motor_speed(100, 100)

if __name__ == '__main__':
    rospy.init_node('sample_listener')
    rospy.Subscriber("/scan", LaserScan, laser_scan_callback)
    print "set subscriber"
    rospy.spin()
