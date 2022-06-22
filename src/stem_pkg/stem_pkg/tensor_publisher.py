import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
import cv2
import tensorflow as tf
import numpy as np
import time
import I2C_LCD_driver
import serial

class TensorPublisher(Node) :
    def __init__(self, interpreter, cap, mylcd):
        super().__init__('tensor_publisher')
        qos_profile = QoSProfile(depth=10)
        ser = serial.Serial('/dev/ttyS0', 115200)
        mylcd.lcd_display_string("",2)
        self.tensor_publisher = self.create_publisher(
            String,
            'tflite_result',
            qos_profile)
        big, small = self.max_tensor(interpreter, cap, mylcd)
        data = "!"+ '{0:0^3}'.format(f'{small}') + '{0:0^3}'.format(f'{big}') +"!"
        ser.write(data.encode())
        mylcd.lcd_display_string("",2)
        mylcd.lcd_display_string("Started",2)

        while cap.isOpened():
            self.tensor_result(interpreter, cap)

    def max_tensor(self, interpreter, cap, mylcd) :
        start_time = time.time()
        big = 0
        small = float('inf')
        while (now <= 5) and cap.isOpened() :
            now = time.time() - start_time
            now = int(now)
            mylcd.lcd_display_string("",2)
            mylcd.lcd_display_string(f'Started in {now} sec',2)
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
            return int(big), int(small)

    def tensor_result(self, interpreter, cap) :
        _, frame = cap.read()
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
        y, x, c = frame.shape
        data = list()
        shaped = np.squeeze(np.multiply(keypoints, [y, x, 100]))
        for shape in shaped :
            data += shape.tolist()
        datastr = [f'{int(x)}' for x in data]
        datastr = ["^"] + datastr
        msg.data = "*".join(datastr)
        self.tensor_publisher.publish(msg)
        self.get_logger().info('Published data : {}'.format(msg.data))

def main(args=None) :
    rclpy.init(args=args)
    interpreter = tf.lite.Interpreter(model_path="lite-model_movenet_singlepose_lightning_3.tflite")
    interpreter.allocate_tensors()
    cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
    mylcd = I2C_LCD_driver.lcd()
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