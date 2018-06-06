#!/usr/bin/env python
# import roslib
# roslib.load_manifest('ros_kagotos')
import rospy
from sensor_msgs.msg import LaserScan

current_data = None

def laser_scan_callback(data):
    print "get laser info"
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    print len(data.intensities)
    current_data = data

def set_subscriber():
    rospy.init_node('sample_listener')
    rospy.Subscriber("/scan", LaserScan, laser_scan_callback)
    print "set subscriber"
    rospy.spin()

def set_server():
    print "set server"

if __name__ == '__main__':
    set_subscriber()

