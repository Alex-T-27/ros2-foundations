import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist 

class Driver(Node):
    def __init__(self):
        super().__init__('driver')
        
        self.declare_parameter('linear_speed', 0.2)
        self.declare_parameter('angular_speed', 0.5)

        self.lin = self.get_parameter('linear_speed').value
        self.ang = self.get_parameter('angular_speed').value

        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)

        self.create_timer(0.1, self.twist)

    def twist(self):
        msg = Twist()
        msg.linear.x = self.lin
        msg.angular.z = self.ang
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




