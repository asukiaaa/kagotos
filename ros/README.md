# kagotos/ros

message test.
```
rostopic pub -r 10 /base_controller geometry_msgs/Twist  '{linear:  {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'
```

References:
- [How to publish a ROS msg on Linux terminal](https://answers.ros.org/question/218818/how-to-publish-a-ros-msg-on-linux-terminal/)
