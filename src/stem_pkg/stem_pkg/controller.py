import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
import RPi.GPIO as GPIO

class Controller(Node) :
    def __init__(self):
        super().__init__('controller')
        qos_profile = QoSProfile(depth=10)
        self.controller = self.create_publisher(
            String,
            'key_command',
            qos_profile)
        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #RED
        GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #ORANGE

        GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #YELLOW
        GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #GREEN

        GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #BLUE
        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #VIOLET

        GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #BROWN

        #GPIO.setup(17, GPIO.IN, GPIO.PUD_UP) #black toggle yellow
        #GPIO.setup(18, GPIO.IN, GPIO.PUD_UP) #black toggle greeen

        GPIO.add_event_detect(12, GPIO.FALLING, callback = self.on_press, bouncetime=100)
        GPIO.add_event_detect(13, GPIO.FALLING, callback = self.on_press, bouncetime=100)

        GPIO.add_event_detect(19, GPIO.FALLING, callback = self.on_press, bouncetime=100)
        GPIO.add_event_detect(16, GPIO.FALLING, callback = self.on_press, bouncetime=100)

        GPIO.add_event_detect(20, GPIO.FALLING, callback = self.on_press, bouncetime=100)
        GPIO.add_event_detect(26, GPIO.FALLING, callback = self.on_press, bouncetime=100)

        GPIO.add_event_detect(21, GPIO.FALLING, callback = self.on_press, bouncetime=100)

        # GPIO.add_event_detect(17, GPIO.FALLING, callback = self.on_press, bouncetime=100)
        # GPIO.add_event_detect(18, GPIO.FALLING, callback = self.on_press, bouncetime=100)
        #GPIO.wait_for_edge(18, GPIO.RISING, bouncetime = 10)

    def publish_key_command_msg(self, msg) :
        self.controller.publish(msg)
        self.get_logger().info('Published command message: {0}'.format(msg.data))

    def on_press(self, channel):
        msg = String()
        msg.data = '{}'.format(self.command_maker(channel))
        if msg.data is not None :
            self.publish_key_command_msg(msg)

    def command_maker(self, k):
        c = String()
        if k == 12 :
            c = "up"
        elif k == 13 :
            c = "left"
        elif k == 19 :
            c = "init"
        elif k == 16 :
            c = "down"
        elif k == 20 :
            c = "turn left"
        elif k == 26 :
            c = "turn right"
        elif k == 21 :
            c = "right"
        elif k == 18 :
            c = "True"
        elif k == 17 :
            c = "False"
        else :
            c = None
        return c


def main(args=None) :
    rclpy.init(args=args)
    node = Controller()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        GPIO.cleanup()
        rclpy.shutdown()

if __name__ == '__main__' :
    main()