# kagotos/ros

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
