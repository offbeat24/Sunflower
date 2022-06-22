from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sf_pkg',
            executable='tensor_publisher',
            name='tensor_publisher'
            #output= 'screen'
            ),

        Node(
            package='sf_pkg',
            executable='calculator',
            name='calculator',),

        Node(
            package='sf_pkg',
            executable='cmd_selector',
            name='cmd_selector' ),

        Node(
            package='sf_pkg',
            executable='serial_talker',
            name='serial_talker',
            output= 'screen' )
    ])