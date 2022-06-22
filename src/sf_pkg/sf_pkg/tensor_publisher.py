import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
import cv2
import tensorflow as tf
import numpy as np
#import I2C_LCD_driver
import serial
import time


# i2c bus (0 -- original Pi, 1 -- Rev 2 Pi)
I2CBUS = 1
# LCD Address
ADDRESS = 0x27
import smbus
from time import sleep
class i2c_device:
   def __init__(self, addr, port=I2CBUS):
      self.addr = addr
      self.bus = smbus.SMBus(port)
# Write a single command
   def write_cmd(self, cmd):
      self.bus.write_byte(self.addr, cmd)
      sleep(0.0001)
# Write a command and argument
   def write_cmd_arg(self, cmd, data):
      self.bus.write_byte_data(self.addr, cmd, data)
      sleep(0.0001)
# Write a block of data
   def write_block_data(self, cmd, data):
      self.bus.write_block_data(self.addr, cmd, data)
      sleep(0.0001)
# Read a single byte
   def read(self):
      return self.bus.read_byte(self.addr)
# Read
   def read_data(self, cmd):
      return self.bus.read_byte_data(self.addr, cmd)
# Read a block of data
   def read_block_data(self, cmd):
      return self.bus.read_block_data(self.addr, cmd)
# commands
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80
# flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00
# flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00
# flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00
# flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00
# flags for backlight control
LCD_BACKLIGHT = 0x08
LCD_NOBACKLIGHT = 0x00
En = 0b00000100 # Enable bit
Rw = 0b00000010 # Read/Write bit
Rs = 0b00000001 # Register select bit
class lcd:
   #initializes objects and lcd
   def __init__(self):
      self.lcd_device = i2c_device(ADDRESS)
      self.lcd_write(0x03)
      self.lcd_write(0x03)
      self.lcd_write(0x03)
      self.lcd_write(0x02)
      self.lcd_write(LCD_FUNCTIONSET | LCD_2LINE | LCD_5x8DOTS | LCD_4BITMODE)
      self.lcd_write(LCD_DISPLAYCONTROL | LCD_DISPLAYON)
      self.lcd_write(LCD_CLEARDISPLAY)
      self.lcd_write(LCD_ENTRYMODESET | LCD_ENTRYLEFT)
      sleep(0.2)
   # clocks EN to latch command
   def lcd_strobe(self, data):
      self.lcd_device.write_cmd(data | En | LCD_BACKLIGHT)
      sleep(.0005)
      self.lcd_device.write_cmd(((data & ~En) | LCD_BACKLIGHT))
      sleep(.0001)
   def lcd_write_four_bits(self, data):
      self.lcd_device.write_cmd(data | LCD_BACKLIGHT)
      self.lcd_strobe(data)
   # write a command to lcd
   def lcd_write(self, cmd, mode=0):
      self.lcd_write_four_bits(mode | (cmd & 0xF0))
      self.lcd_write_four_bits(mode | ((cmd << 4) & 0xF0))
   # write a character to lcd (or character rom) 0x09: backlight | RS=DR<
   # works!
   def lcd_write_char(self, charvalue, mode=1):
      self.lcd_write_four_bits(mode | (charvalue & 0xF0))
      self.lcd_write_four_bits(mode | ((charvalue << 4) & 0xF0))
  
   # put string function with optional char positioning
   def lcd_display_string(self, string, line=1, pos=0):
    if line == 1:
      pos_new = pos
    elif line == 2:
      pos_new = 0x40 + pos
    elif line == 3:
      pos_new = 0x14 + pos
    elif line == 4:
      pos_new = 0x54 + pos
    self.lcd_write(0x80 + pos_new)
    for char in string:
      self.lcd_write(ord(char), Rs)
   # clear lcd and set to home
   def lcd_clear(self):
      self.lcd_write(LCD_CLEARDISPLAY)
      self.lcd_write(LCD_RETURNHOME)
   # define backlight on/off (lcd.backlight(1); off= lcd.backlight(0)
   def backlight(self, state): # for state, 1 = on, 0 = off
      if state == 1:
         self.lcd_device.write_cmd(LCD_BACKLIGHT)
      elif state == 0:
         self.lcd_device.write_cmd(LCD_NOBACKLIGHT)
   # add custom characters (0 - 7)
   def lcd_load_custom_chars(self, fontdata):
      self.lcd_write(0x40);
      for char in fontdata:
         for line in char:
            self.lcd_write_char(line)   

class TensorPublisher(Node) :
    def __init__(self, interpreter, cap, mylcd):
        super().__init__('tensor_publisher')
        qos_profile = QoSProfile(depth=10)
        ser = serial.Serial('/dev/ttyS0', 115200)
        mylcd.lcd_display_string(f'Sunflower',1)
        self.tensor_publisher = self.create_publisher(
            String,
            'tflite_result',
            qos_profile)
        big, small = self.max_tensor(interpreter, cap, mylcd)
        data = "!"+ '{0:0>3}'.format(f'{small}') + '{0:0>3}'.format(f'{big}') +"!"
        ser.write(data.encode())
        self.get_logger().info('Initialized data : {}'.format(data))

        while cap.isOpened():
            self.tensor_result(interpreter, cap, mylcd)

    def max_tensor(self, interpreter, cap, mylcd) :
        start_time = time.time()
        big = 0
        small = 100
        while (time.time() - start_time <= 5) and cap.isOpened() :
            now = time.time() - start_time
            now = 5 - int(now)
            mylcd.lcd_display_string("",2)
            mylcd.lcd_display_string(f'{now}',2)
            _, frame = cap.read()
            y, x, _ = frame.shape
            # 첫. 이름 // 둘. 이미지
            # Reshape img
            # 192 x 192 x 3
            img = frame.copy()
            img = tf.image.resize_with_pad(np.expand_dims(img, axis=0), 192, 192)
            input_image = tf.cast(img, dtype=tf.float32)
            # Setup input and output
            input_details = interpreter.get_input_details()
            output_details = interpreter.get_output_details()
            # Mode Predictions
            interpreter.set_tensor(input_details[0]['index'], np.array(input_image))
            interpreter.invoke()
            tmp = interpreter.get_tensor(output_details[0]['index'])
            keypoints = tmp[0][0][1:3]
            data = list()
            shaped = np.squeeze(np.multiply(keypoints, [y, x, 100]))
            for shape in shaped :
                data += shape.tolist()
            l_x, l_y, l_c, r_x, r_y, r_c = map(lambda x : x, data)
            if (l_c > 0.4) and (r_c > 0.4):
            # length를 float으로 보내도 되쥬?
                length = ((l_x - r_x) ** 2 + (l_y - r_y) ** 2) ** (1 / 2)
                big = max(length, big)
                small = min(length, small)
        else :
            mylcd.lcd_display_string("Started",2)
            return int(big), int(small)

    def tensor_result(self, interpreter, cap, mylcd) :
        ret, frame = cap.read()
        # 첫. 이름 // 둘. 이미지
        # Reshape img
        # 192 x 192 x 3
        img = frame.copy()
        img = tf.image.resize_with_pad(np.expand_dims(img, axis=0), 192, 192)
        input_image = tf.cast(img, dtype=tf.float32)
        # Setup input and output
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        # Mode Predictions
        interpreter.set_tensor(input_details[0]['index'], np.array(input_image))
        interpreter.invoke()
        tmp = interpreter.get_tensor(output_details[0]['index'])
        keypoints_with_scores = tmp[0][0]
        self.draw_keypoints(frame, keypoints_with_scores[:3])

    def draw_keypoints(self, frame, keypoints):
        msg = String()
        y, x, _ = frame.shape
        data = list()
        shaped = np.squeeze(np.multiply(keypoints, [y, x, 100]))
        for shape in shaped :
            data += shape.tolist()
        datastr = [f'{int(x)}' for x in data]
        msg.data = "*".join(datastr)
        self.tensor_publisher.publish(msg)
        self.get_logger().info('Published data : {}'.format(msg.data))

def main(args=None) :
    rclpy.init(args=args)
    interpreter = tf.lite.Interpreter(model_path="lite-model_movenet_singlepose_lightning_3.tflite")
    interpreter.allocate_tensors()
    cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
    mylcd = lcd()
    node = TensorPublisher(interpreter, cap, mylcd)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        cap.release()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__' :
    main()

#코, 왼눈, 오눈, 왼귀, 오귀, 왼어깨, 오어깨