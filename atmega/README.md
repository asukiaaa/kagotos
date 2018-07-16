# kagotos/atmega

# Components
- Pro Micro (Arduino Lernardo compatible)
- Motor Driver
- Gear motors and tires

# Requirement

platformIO

# Usage

## Build
```
pio run
```

## Write
```
pio run -t upload
```

## Test

Start subscriber.
```
roscore
```

```
rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=115200
```

Send geometry_msg::Twist.

Forward.
```
rostopic pub /cmd_vel geometry_msgs/Twist  '{linear:  {x: 1.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}' --once
```

Back.
```
rostopic pub /cmd_vel geometry_msgs/Twist  '{linear:  {x: -1.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}' --once
```

Turn left.
```
rostopic pub /cmd_vel geometry_msgs/Twist  '{linear:  {x: 1.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.0}}' --once
```

Turn right.
```
rostopic pub /cmd_vel geometry_msgs/Twist  '{linear:  {x: 1.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: -1.0}}' --once
```

Or use [teleop_twist_keyboard](https://github.com/ros-teleop/teleop_twist_keyboard) to publish Twist for cmd_vel.

# Setup memo

```
cd [kagotos dir]
mkdir arduino
cd arduino
pio init --board sparkfun_promicro16
```

# License
MIT

# References
- [rosserial_arduino Hello World](http://wiki.ros.org/rosserial_arduino/Tutorials/Hello%20World)
- [rosserial_arduino Blink](http://wiki.ros.org/rosserial_arduino/Tutorials/Blink)
