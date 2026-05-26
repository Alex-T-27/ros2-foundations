import time 
import rclpy
from rclpy.node import Node 
from rclpy.action import ActionServer
from example_interfaces.action import Fibonacci

class FibServer(Node):
    def __init__(self):
        super().__init__('fib_server')
        self._srv =ActionServer(self, Fibonacci, 'fibonacci', self.execute)

    def execute(self, goal_handle):
        order = goal_handle.request.order
        seq = [0,1]

        feedback = Fibonacci.Feedback()

        for i in range (2, order):
            seq.append(seq[(i-1)]+seq[(i-2)])
            feedback.sequence = seq
            goal_handle.publish_feedback(feedback)
            time.sleep(0.5)

        goal_handle.succeed()

        result = Fibonacci.Result()
        result.sequence = seq
        return result

def main():
    rclpy.init()
    rclpy.spin(FibServer())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
