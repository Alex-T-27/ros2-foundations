import rclpy
from rclpy.node import Node 
from rclpy.action import ActionClient
from turtlesim.action import RotateAbsolute

class RotateClient(Node):
    def __init__(self):
        super().__init__('rotate_client')
        self._client = ActionClient(self, RotateAbsolute, '/turtle1/rotate_absolute')

    def send_goal(self, theta):
        self._client.wait_for_server()

        goal = RotateAbsolute.Goal()

        goal.theta = theta
        
        future = self._client.send_goal_async(goal, feedback_callback = self.on_feedback)
        return future

    def on_feedback(self, fb):
        self.get_logger().info(f'remaining: {fb.feedback.remaining:.2f}')
        pass

def main():
    rclpy.init()
    node = RotateClient()

    future = node.send_goal(1.57)  # ~90°
    rclpy.spin_until_future_complete(node, future)

    goal_handle = future.result()
    # goal accepted? get the result future
    result_future = goal_handle.get_result_async()
    rclpy.spin_until_future_complete(node, result_future)

    result = result_future.result().result
    node.get_logger().info(f'done, delta={result.delta}')

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
