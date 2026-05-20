from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

    Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='sim',
    ),

    Node(
        package='topics_demo',
        executable='driver', 
        name='driver',
        remappings=[('cmd_vel', '/turtle1/cmd_vel')]
        # TODO: your driver publishes on relative topic 'cmd_vel'.
        #       turtlesim listens on '/turtle1/cmd_vel'.
        #       Add a remappings= argument to bridge them.
        #       It's a list of (from, to) tuples.
    )
    ])
