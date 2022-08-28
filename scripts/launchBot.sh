source /opt/ros/humble/setup.bash
source ~/lawnMowBot/install/setup.bash
source ~/rpLidarROS2/rplidarTest/rplidar_ros/install/setup.bash

ros2 launch nav2_bringup navigation_launch.py && ros2 launch slam_toolbox online_asynch_launch.py