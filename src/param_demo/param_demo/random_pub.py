import rclpy
from rclpy.node import Node
import random

class RandomNumber(Node):
    def __init__(self):
        super().__init__('a_random_num')
        self.create_timer(
            0.5,
            self.tick,
        )
    def tick(self):
        num = random.randint(0,100)
        num_str = str(num)
        self.get_logger().info(num_str)
        pass

def main(argc=None):
    rclpy.init(args=argc)
    node = RandomNumber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
