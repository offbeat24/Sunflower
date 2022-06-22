import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
import asyncio
import serial_asyncio


class SerialTalker(Node):
    SERIAL_PORT = '/dev/ttyS0'
    def __init__(self):
        super().__init__('serial_node')
        qos_profile = QoSProfile(depth=10)
        print('Writer created')
        self.serial_node = self.create_subscription(
            String,
            'command',
            self.command_main,
            qos_profile)
        self.get_logger().info("Serial connection started")

    async def command_main(self, msg):
        self.get_logger().info('Received data : {}'.format(msg.data))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.serial_message(msg.data))
        loop.close()

    async def connection_made(self):
        _, writer = await serial_asyncio.open_serial_connection(url=self.SERIAL_PORT, baudrate=115200)
        print('Writer created')
        return writer

    async def serial_message(self, msg):
        writer = await self.connection_made()
        sent = await self.send(writer, msg)
        await asyncio.wait(sent)

    async def send(self, writer, msg) :
        for c in msg :
            writer.write(c.encode())
            self.get_logger().info(f'sent: {c} in {msg}')
        #writer.write(b'_')
        self.get_logger().info('complete')


def main(args=None):
    rclpy.init(args=args)
    node = SerialTalker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__' :
    main()