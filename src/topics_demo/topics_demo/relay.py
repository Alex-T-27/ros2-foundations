import rclpy
from rclpy.node import Node 
from std_msgs.msg import String

class Relay(Node):
    def __init__(self):
        super().__init__('relay')

        self.pub = self.create_publisher(String, '/shouter_upper', 10)

        self.sub = self.create_subscription(String, '/shouter', self.on_msg, 10)
        
    def on_msg(self, msg):
        upper_str = String()
        upper_str.data = msg.data.upper()
        self.pub.publish(upper_str)
        self.get_logger().info(f'Upper string: {upper_str.data}')
        
def main():
    rclpy.init()
    node = Relay()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
