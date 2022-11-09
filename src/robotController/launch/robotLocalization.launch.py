import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    
    
    pkg_share = FindPackageShare(package='hadabot_description').find('hadabot_description')
    
    robot_localization_file_path = os.path.join(pkg_share, 'config/ekf.yaml') 
    use_sim_time = LaunchConfiguration('use_sim_time')

  
    start_robot_localization_cmd = Node(
        package='robot_localization',
        executable='ukf_node',
        name='ukf_filter_node',
        output='screen',
        parameters=[robot_localization_file_path, 
        {'use_sim_time': use_sim_time}])
    
    
    
    

    # Run the node
    return LaunchDescription([
        start_robot_localization_cmd
    ])

    

