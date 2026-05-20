import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class SpawnClient(Node):
    def __init__(self):
        super().__init__('spawn_client')

        self.cli = self.create_client(Spawn, '/spawn')

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('waiting for /spawn server...')
            

    def send_request(self, x,  y, name):
        req = Spawn.Request()
        req.x =  x 
        req.y = y 
        req.theta = 0 #I assume there's a function to calculate theta based on x and y
        req.name = name
        return self.cli.call_async(req)

def main():
    rclpy.init()
    node = SpawnClient()

    future = node.send_request(4.0, 2.0, 'leo')
    rclpy.spin_until_future_complete(node,future)

    response = future.result()

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

