import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String

class CommandSelector(Node):
    tensor_flag = False
    def __init__(self):
        super().__init__('command_selector')
        qos_profile = QoSProfile(depth=10)
        self.tflite_subscriber = self.create_subscription(
            String,
            'tf_command',
            self.subscribe_tflite,
            qos_profile)

        self.command_publisher = self.create_publisher(
            String,
            'command',
            qos_profile)

        self.key_subscriber = self.create_subscription(
            String,
            'key_command',
            self.subscribe_key,
            qos_profile)

    def subscribe_tflite(self, msg):
        self.command_toNucleo(msg.data)

    def subscribe_key(self, msg):
        self.get_logger().info('Received from key: {0}'.format(msg.data))
        self.command_toNucleo(msg.data)

    def command_toNucleo(self, cmd):
        msg = String()
        msg.data = cmd
        self.command_publisher.publish(msg)
        self.get_logger().info('Published command: {}'.format(msg.data))



def main(args=None):
    rclpy.init(args=args)
    node = CommandSelector()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__' :
    main()