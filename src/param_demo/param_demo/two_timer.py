import rclpy
from rclpy.node import Node
import random

class TwoTimer(Node):
    def __init__(self):
        super().__init__('a_random_num')
        self.create_timer(
            0.5,
            self.fast_tick,
        )
        self.create_timer(
            2,
            self.slow_tick,
        )
    def slow_tick(self):
        self.get_logger().info('slow')

    def fast_tick(self):
        self.get_logger().info('fast')


def main(argc=None):
    rclpy.init(args=argc)
    node = TwoTimer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
