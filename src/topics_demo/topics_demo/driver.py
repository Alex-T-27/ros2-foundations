import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist 

class Driver(Node):
    def __init__(self):
        super().__init__('driver')

        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)

        self.create_timer(0.5, self.twist)

    def twist(self):
        msg = Twist()
        msg.linear.x = 0.2
        msg.angular.z = 0.5
        self.pub.publish(msg)
        self.get_logger().info(f'cmd: vx={msg.linear.x}, wz= {msg.angular.z}')

def main():
    rclpy.init()
    node = Driver()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()




