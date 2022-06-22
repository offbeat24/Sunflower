import cv2
import tensorflow as tf
import numpy as np
import math
def step_motor(data):
    n_x, n_y, n_con, l_x, l_y, l_con, r_x, r_y, r_con = map(lambda x: int(x), data)
    if (n_con > 30) and (l_con > 30) and (r_con > 30):
        # sub_ : 양쪽 눈 연결하는 .벡터
        sub_x = l_x - r_x
        sub_y = l_y - r_y
        # cen_ : 눈 사이의 중심 .점
        cen_x = (l_x + r_x) / 2
        cen_y = (l_y + r_y) / 2
        # ang_ : 코에서 cen_ 을 향하는 .벡터
        ang_x = cen_x - n_x
        ang_y = cen_y - n_y
        # 벡터 내적
        # u, v : ang_ , sub_ 벡터의 크기
        u = math.sqrt(ang_x * ang_x + ang_y * ang_y)
        v = math.sqrt(sub_x * sub_x + sub_y * sub_y)
        # mul : 위 내적값
        mul = (ang_x * sub_x) + (ang_y * sub_y)
        # cos_theta: cos값
        # theta : 끼인각
        cos_theta = mul / (u * v)
        theta = math.acos(cos_theta)
        theta = (theta * 180) / math.pi
    else:
        # 3점 모두 신뢰도 0.4보다 작을때
        theta = 200
    return int(theta) *1000
    
def lin2_motor(nose):
    _ , nose_x, nose_confidence = map(lambda x: int(x), nose)
    # 리니어 모터 작동 mode : 1,2,3
    # 임의의 쓰레기 값
    state = 4
    if nose_confidence > 40:
        # x 좌표값 [0 640] : 100의 자리수로 영역 나누기
        nose_x //= 100
        if (nose_x == 0) or (nose_x == 1) or (nose_x == 2):
            state = 3
        elif (nose_x == 3) :
            state = 2
        elif (nose_x == 4) or (nose_x == 5) or (nose_x == 6):
            state = 1
    else:
        # 중심에 있는지 판단 어려워도 데이터 계속 보내는게 낫겠죠?
        state = 4
    return state*1000000

def eye_dist(eye) :
        l_x, l_y, l_c, r_x, r_y, r_c = map(lambda x : int(x), eye)
        if (l_c > 0.4) and (r_c > 0.4):
        # length를 float으로 보내도 되쥬?
            length = ((l_x - r_x) ** 2 + (l_y - r_y) ** 2) ** (1 / 2)
        else :
            length = 999
        return int(length)

interpreter = tf.lite.Interpreter(model_path="lite-model_movenet_singlepose_lightning_3.tflite")
interpreter.allocate_tensors()
# open camera
cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)

# set dimensions
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# take frame
ret, frame = cap.read()
# write frame to file
cv2.imwrite('./image.jpg', frame)

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
print(keypoints_with_scores[:3])
y, x, _ = frame.shape
data = list()
shaped = np.squeeze(np.multiply(keypoints_with_scores[:3], [y, x, 100]))
for shapes in shaped :
    data += shapes.tolist()
datastr = [f'{int(x)}' for x in data]
toSend = step_motor(datastr) + lin2_motor(datastr[:3]) + eye_dist(datastr[3:9])
print(toSend)
cap.release()

