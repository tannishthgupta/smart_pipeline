import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class ProcessorNode(Node):
    def __init__(self):
        super().__init__('processor_node')

        self.history = []
        self.window_size = 5

        self.subscription = self.create_subscription(
            Int32,
            'raw_data',
            self.process_callback,
            10
        )

        self.publisher_ = self.create_publisher(Int32, 'processed_data', 10)

    def process_callback(self, msg):
        # store incoming data
        self.history.append(msg.data)

        # keep only last N values
        if len(self.history) > self.window_size:
            self.history.pop(0)

        # compute average
        avg = sum(self.history) / len(self.history)

        # create output message
        out_msg = Int32()
        out_msg.data = int(avg)

        # publish
        self.publisher_.publish(out_msg)

        self.get_logger().info(f"Raw: {msg.data} | Smoothed: {out_msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = ProcessorNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
