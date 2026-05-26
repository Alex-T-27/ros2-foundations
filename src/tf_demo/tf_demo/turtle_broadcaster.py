import rclpy
from rclpy.node import Node 
import math
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
from turtlesim.msg import Pose

class TurtleBroadcaster(Node):
    def __init__(self):
        super().__init__('turtle_broadcaster')
        self.br = TransformBroadcaster(self)
        self.create_subscription(Pose, '/turtle1/pose', self.on_pose, 10)

    def on_pose(self,msg):
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'world'
        t.child_frame_id = 'turtle1'

        t.transform.translation.x = msg.x
        t.transform.translation.y = msg.y
        t.transform.translation.z = 0.0

        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = math.sin(msg.theta / 2.0)
        t.transform.rotation.w = math.cos(msg.theta / 2.0)

        self.br.sendTransform(t)

def main():
    rclpy.init()
    rclpy.spin(TurtleBroadcaster())
    rclpy.shutdown()

if __name__ == '__main__':
    main()




