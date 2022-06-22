import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
from pynput import keyboard

class Tester(Node) :
    def __init__(self):
        super().__init__('tester')
        qos_profile = QoSProfile(depth=10)
        self.tester = self.create_publisher(
            String,
            'key_command',
            qos_profile)
        listener = keyboard.Listener(
            on_press = self.on_press,
            on_release = self.on_release)
        listener.start()
        listener.join()

    def publish_key_command_msg(self, msg) :
        self.tester.publish(msg)
        self.get_logger().info('Published command message: {0}'.format(msg.data))

    def on_press(self, key):
        msg = String()
        try:
            k = key.char
        except:
            k = key.name
        msg.data = '{}'.format(self.command_maker(k))
        if msg.data is not None :
            self.publish_key_command_msg(msg)

    def command_maker(self, k):
        c = String()
        if k == "w" :
            c = "up"
        elif k == "s" :
            c = "down"
        elif k == "a" :
            c = "left"
        elif k == "d" :
            c = "right"
        elif k == "," :
            c = "turn left"
        elif k == "." :
            c = "turn right"
        else :
            c = None
        return c

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False

def main(args=None) :
    rclpy.init(args=args)
    node = Tester()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__' :
    main()