import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__('talker')

        self.pub = self.create_publisher(String, 'shouter', 10)

        self.create_timer(2, self.tick)

    def tick(self):
        msg = String()
        msg.data = 'Konichiwa, sekai'
        self.pub.publish(msg)
        self.get_logger().info(f'sent: {msg.data}')

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



