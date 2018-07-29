# kagotos/ros

# Create Map

Install [teleop_twist_keyboard](https://github.com/ros-teleop/teleop_twist_keyboard) to publish Twist for cmd_vel.

Terminal 1 for creating map.
```
roslaunch kagotos hector_mapping_example.launch
```

Terminal 2 for subscribing Twist to move kagotos.
```
rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=115200
```

Terminal 3 for publish Twist to move kagotos.
```
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```

Terminal 4 for saving map.
```
rosrun map_server map_saver -f ./mymap
```

Reference: [ROS hector_slamを使ってマップを作る。](http://morokyuu.way-nifty.com/blog/2016/01/hector_slam-0a5.html)

# Test commands

## Test twist message
message test.
```
rostopic pub -r 10 /base_controller geometry_msgs/Twist  '{linear:  {x: 1, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0,z: 0.0}}'
```

## Check value from remote PC

On robot.

```
export ROS_IP=kagotos3.local
roslaunch ydlidar lidar.launch
```

On remote PC.
```
export ROS_MASTER_URI=http://kagotos3.local:11311
rostopic echo /scan
```

References:
- [How to publish a ROS msg on Linux terminal](https://answers.ros.org/question/218818/how-to-publish-a-ros-msg-on-linux-terminal/)
