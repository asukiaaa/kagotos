#!/usr/bin/env python
# import roslib
# roslib.load_manifest('ros_kagotos')
import rospy
from sensor_msgs.msg import LaserScan
import SimpleHTTPServer
import SocketServer
import thread
import time

PORT = 8000

current_data = None

def laser_scan_callback(data):
    global current_data
    print "get laser info"
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    print len(data.intensities)
    current_data = data

def set_subscriber():
    rospy.init_node('sample_listener')
    rospy.Subscriber("/scan", LaserScan, laser_scan_callback)
    print "set subscriber"
    rospy.spin()

# https://stackoverflow.com/questions/6530979/html-in-do-get-method-of-a-simple-python-webserver
class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        global current_data
        print self.path
        if self.path == '/':
            # self.protocol_version='HTTP/1.1'
            self.send_response(200, 'OK')
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            laser_data = ""
            if current_data != None:
                laser_data = " ".join(map(str,current_data.intensities))
	    self.wfile.write("Hello World ! " + laser_data)

def set_server():
    print "set server"
    Handler = MyRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "serving at port", PORT
    httpd.serve_forever()

if __name__ == '__main__':
    thread.start_new_thread(set_server, ())
    # thread.start_new_thread(set_subscriber, ())
    set_subscriber()
