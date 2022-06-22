from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='stem_pkg',
            executable='tensor',
            name='tensor_publisher',
            output= 'screen'),

        Node(
            package='stem_pkg',
            executable='calculator',
            name='tensor_publisher',),

        Node(
            package='stem_pkg',
            executable='cmd_selector',
            name='cmd_selector' ),

        Node(
            package='stem_pkg',
            executable='serial_talker',
            name='serial_talker',
            output= 'screen' )
    ])