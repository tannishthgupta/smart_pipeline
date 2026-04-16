import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class AlertNode(Node):
    def __init__(self):
        super().__init__('alert_node')

        # Declare parameter
        self.declare_parameter('threshold', 120)
        self.threshold = self.get_parameter('threshold').value

        self.subscription = self.create_subscription(
            Int32,
            'processed_data',
            self.alert_callback,
            10
        )

    def alert_callback(self, msg):
        if msg.data > self.threshold:
            self.get_logger().warn(f"⚠ ALERT! High value: {msg.data}")
        else:
            self.get_logger().info(f"Safe: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = AlertNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()