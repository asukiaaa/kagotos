# kagotos
A project to run a robot named kagotos.

# Requirements
- ROS ([melodic](http://wiki.ros.org/melodic))
- [ydlidar](https://github.com/EAIBOT/ydlidar)
- [rosserial](https://github.com/ros-drivers/rosserial)

# Usage

## Install

```
cd ~/ros_catkin_ws/src
git clone https://github.com/asukiaaa/kagotos.git
cd ../
catkin_make
```

## Run

```
cd ~/ros_catkin_ws
source devel/setup.sh
roslaunch kagotos start.launch
```

# Executed Commands to create this project

```
cd ~/ros_catkin_ws/src
catkin_create_pkg kagotos roscpp rospy tf urdf ydlidar
```

# License
MIT

# References
- [tf/Tutorials/Writing a tf broadcaster (Python)](http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20broadcaster%20%28Python%29)
- [tf/Tutorials/Writing a tf listener (Python)](http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20listener%20%28Python%29)
