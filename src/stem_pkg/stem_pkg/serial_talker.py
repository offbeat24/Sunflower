import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
import serial 


class SerialTalker(Node):
    SERIAL_PORT = '/dev/ttyS0'
    ser = serial.Serial('/dev/ttyS0', 115200)
    def __init__(self):
        super().__init__('serial_talker')
        qos_profile = QoSProfile(depth=10)
        self.serial_talker = self.create_subscription(
            String,
            'command',
            self.serial_message,
            qos_profile)
        self.get_logger().info("Serial connection started")

    def serial_message(self, msg):
        #self.ser.write("^1*2*3*4*5*6*7*8*8".encode())
        #self.get_logger().info('Transmitted')
        self.get_logger().info('Transmitted data : {}'.format(msg.data))
        self.ser.write(msg.data.encode())


def main(args=None):
    rclpy.init(args=args)
    node = SerialTalker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.ser.close()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__' :
    main()