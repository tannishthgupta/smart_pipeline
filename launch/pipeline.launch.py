from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        Node(
            package='smart_pipeline',
            executable='sensor',
            name='sensor_node'
        ),

        Node(
            package='smart_pipeline',
            executable='processor',
            name='processor_node'
        ),

        Node(
            package='smart_pipeline',
            executable='alert',
            name='alert_node',
            parameters=[{'threshold': 100}]
        ),
    ])
