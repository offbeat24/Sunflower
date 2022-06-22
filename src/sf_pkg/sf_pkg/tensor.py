import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from sunflower_interfaces.msg import TfliteResult
import cv2
import tensorflow as tf
import numpy as np

class Tensor(Node) :
    def __init__(self, interpreter, cap):
        super().__init__('tensor')
        qos_profile = QoSProfile(depth=10)
        self.tensor = self.create_publisher(
            TfliteResult,
            'tensor_result',
            qos_profile)
        while cap.isOpened():
            self.tensor_result(interpreter, cap)

    def tensor_result(self, interpreter, cap) :
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
        self.draw_keypoints(frame, keypoints_with_scores[:7])

    def draw_keypoints(self, frame, keypoints):
        msg = TfliteResult()
        y, x, c = frame.shape
        data = list()
        shaped = np.squeeze(np.multiply(keypoints, [y, x, 1]))
        msg.nose = shaped[0].tolist()
        msg.eye_l = shaped[1].tolist()
        msg.eye_r = shaped[2].tolist()
        msg.ear_l = shaped[3].tolist()
        msg.ear_r = shaped[4].tolist()
        msg.shoulder_l = shaped[5].tolist()
        msg.shoulder_r = shaped[6].tolist()
        self.tensor.publish(msg)
        self.get_logger().info('Tensor data Published')

def main(args=None) :
    rclpy.init(args=args)
    interpreter = tf.lite.Interpreter(model_path="lite-model_movenet_singlepose_lightning_3.tflite")
    interpreter.allocate_tensors()
    cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
    node = Tensor(interpreter, cap)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__' :
    main()

#코, 왼눈, 오눈, 왼귀, 오귀, 왼어깨, 오어깨