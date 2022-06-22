import cv2
import tensorflow as tf
import numpy as np
# from matplotlib import pyplot as plt
import pickle
import pandas as pd


def triangle(x_1, x_2, x_3, y_1, y_2, y_3):
    first = (x_1 * y_2) + (x_2 * y_3) + (x_3 * y_1)
    second = (x_2 * y_1) + (x_3 * y_2) + (x_1 * y_3)
    result = (first - second) * 0.5
    if result >= 0:
        return result
    else:
        return result * -1


def save_keypoints(frame, keypoints, confidence_threshold):
    y, x, c = frame.shape
    shaped = np.squeeze(np.multiply(keypoints, [y, x, 1]))
    global count
    for kp in shaped:
        ky, kx, kp_conf = kp
        if kp_conf > confidence_threshold:
            int_x = int(kx)
            int_y = int(ky)


def draw_keypoints(frame, keypoints, confidence_threshold):
    y, x, c = frame.shape
    shaped = np.squeeze(np.multiply(keypoints, [y, x, 1]))

    for kp in shaped:
        ky, kx, kp_conf = kp
        if kp_conf > confidence_threshold:
            int_x = int(kx)
            int_y = int(ky)
            cv2.circle(frame, (int_x, int_y), 4, (0, 255, 0), -1)


def draw_connection(frame, keypoints, edges, confidence_threshold):
    y, x, c = frame.shape
    shaped = np.squeeze(np.multiply(keypoints, [y, x, 1]))

    for edge, color in edges.items():
        p1, p2 = edge
        y1, x1, c1 = shaped[p1]
        y2, x2, c2 = shaped[p2]

        if (c1 > confidence_threshold) & (c2 > confidence_threshold):
            cv2.line(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)


EDGES = {
    (0, 1): 'm',
    (0, 2): 'm',
    (1, 3): 'm',
    (2, 4): 'm',
    (0, 5): 'm',
    (0, 6): 'm',
    (5, 7): 'm',
    (7, 9): 'm',
    (6, 8): 'm',
    (8, 10): 'm',
    (5, 6): 'm',
    (5, 11): 'm',
    (6, 12): 'm',
    (11, 12): 'm',
    (11, 13): 'm',
    (13, 15): 'm',
    (12, 14): 'm',
    (14, 16): 'm'
}


# loading model - interpreter is just obj
interpreter = tf.lite.Interpreter(model_path="./lite-model_movenet_singlepose_lightning_3.tflite")

# interpreter = tf.lite.Interpreter(model_path="")
# posenet1 : posenet_mobilenet_v1_100_257x257_multi_kpt_stripped.tflite
# posenet2 : posenet_mobilenet_float_075_1_default_1.tflite
interpreter.allocate_tensors()

# make detections
cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)# connect with cam
# video.mp4로도 변수 넘길수 있음

count = 0
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
x5 = []
y5 = []
x6 = []
y6 = []
x7 = []
y7 = []
while cap.isOpened():# 열린동안
    # read 하기
    ret, frame = cap.read()
    # cv2.imwrite('./image1.jpg', frame)
    # 첫. 이름 // 둘. 이미지
    # 채널 수는 480 x 640 x 3...?

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
    keypoints_with_scores = interpreter.get_tensor(output_details[0]['index'])
    # print(keypoints_with_scores)
    print(keypoints_with_scores)

    # Rendering
    # draw_connection(frame, keypoints_with_scores, EDGES, 0.4)
    # draw_keypoints(frame, keypoints_with_scores, 0.4)
    # save_keypoints(frame, keypoints_with_scores, 0.4)
    # 캠에서 인식된 포인트의 가장 작은 값보다 좀 더 작게

    # cv2.imshow("MoveNet Lightening", frame)
    
    if cv2.waitKey(10) & 0XFF == ord('q'):

        df = pd.DataFrame({"x": [x1, x2, x3, x4, x5, x6, x7],
                           "y": [y1, y2, y3, y4, y5, y6, y7]})
        df.to_pickle("df.pkl")
        # q가 눌렸는지 확인
        break
cap.release()
cv2.destroyAllWindows()