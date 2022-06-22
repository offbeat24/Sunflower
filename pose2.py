import cv2
import tensorflow as tf
# import tensorflow_hub as hub
import numpy as np
# import pickle
import pandas as pd


def triangle(x_1, x_2, x_3, y_1, y_2, y_3):
    first = (x_1 * y_2) + (x_2 * y_3) + (x_3 * y_1)
    second = (x_2 * y_1) + (x_3 * y_2) + (x_1 * y_3)
    result = (first - second) * 0.5
    return result


def save_keypoints(frame3, keypoints3, confidence_threshold):
    y, x, c = frame3.shape
    shaped = np.squeeze(np.multiply(keypoints3, [y, x, 1]))

    count = 0
    temp = []
    for kp in shaped:
        ky, kx, kp_conf = kp
        if kp_conf > confidence_threshold:
            count += 1
            temp.append([kx, ky])
            # int_y = int(ky)
        else:
            continue
    if count == 7:
        left = triangle(temp[0][0], temp[1][0], temp[3][0], temp[0][1], temp[1][1], temp[3][1])
        # triangle(x_1, x_2, x_3, y_1, y_2, y_3)
        right = triangle(temp[4][0], temp[2][0], temp[0][0], temp[4][1], temp[2][1], temp[0][1])
        # center = triangle(temp[4][0], temp[2][0], temp[0][0], temp[4][1], temp[2][1], temp[0][1])
        print(left, right)
        return [(left / right), left, right]


def draw_keypoints(frame1, keypoints1, confidence_threshold):
    y, x, c = frame1.shape
    shaped = np.squeeze(np.multiply(keypoints1, [y, x, 1]))
    print(shaped)
    left_sh = 0
    right_sh = 0
    for kp in shaped:
        state = 0
        state_1 = 0
        ky, kx, kp_conf = kp
        state_1 += 1
        if kp_conf > confidence_threshold:
            int_x = int(kx)
            int_y = int(ky)
            print(int_x, int_y)
            cv2.circle(frame1, (int_x, int_y), 4, (0, 255, 0), -1)
            state += 1
            if (state == state_1) and (state == 5):
                left_sh = int_x
            elif (state == state_1) and (state == 6):
                right_sh = int_x
                return left_sh - right_sh


def draw_connection(frame2, keypoints2, edges, confidence_threshold):
    y, x, c = frame2.shape
    shaped = np.squeeze(np.multiply(keypoints2, [y, x, 1]))

    for edge, color in edges.items():
        p1, p2 = edge
        y1, x1, c1 = shaped[p1]
        y2, x2, c2 = shaped[p2]

        if (c1 > confidence_threshold) & (c2 > confidence_threshold):
            cv2.line(frame2, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)


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
interpreter = tf.lite.Interpreter(model_path="lite-model_movenet_singlepose_lightning_3.tflite")

# interpreter = tf.lite.Interpreter(model_path="")
# posenet1 : posenet_mobilenet_v1_100_257x257_multi_kpt_stripped.tflite
# posenet2 : posenet_mobilenet_float_075_1_default_1.tflite
interpreter.allocate_tensors()

# make detections
cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
# connect with cam
# video.mp4로도 변수 넘길수 있음
Rates = [0]
_Second_Linear_Motor = [-2, -1, 0, 1, 2]
while cap.isOpened():
    # 열린 동안
    # read 하기
    ret, frame = cap.read()
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
    print(keypoints_with_scores)

    # Rendering
    draw_connection(frame, keypoints_with_scores[:][:][:7], EDGES, 0.4)
    center = draw_keypoints(frame, keypoints_with_scores[:][:][:7], 0.4)
    Rate_Le_Ri = list()
    Rate_Le_Ri.append(save_keypoints(frame, keypoints_with_scores[0][0][:7], 0.4))
    Rate_Le_Ri.append(center)
    # [:7] 하면 7개 점만 넘어 가야 되는거 아닝교 왜 계속 팔꿈치 점도 찍
    Rates.append(Rate_Le_Ri)

    # new_rate.append(Rate)
    # 캠에서 인식된 포인트의 가장 작은 값보다 좀 더 작게

    cv2.imshow("MoveNet Lightening", frame)

    if cv2.waitKey(20) & 0XFF == ord('q'):

        # pickle이든 txt든 일단 각도 값을 어디다 저장 ㄱ
        new_rate = pd.DataFrame(Rates, columns=['ratio', 'left area', 'right area', 'center'])
        print(new_rate)
        new_rate.to_pickle("df.pkl")

        # q가 눌렸는지 확인
        break
cap.release()
cv2.destroyAllWindows()