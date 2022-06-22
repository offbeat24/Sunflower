import math


def step_motor(n_x, n_y, l_x, l_y, r_x, r_y):

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
    cos_theta = mul / (u*v)
    theta = math.acos(cos_theta)
    theta = (theta * 180) / math.pi

    return theta


# 코의 x좌표로 프레임상 얼굴 중심 찾기
def lin2_motor(nose_x, nose_confidence):

    # 리니어 모터 작동 mode : 1,2,3
    # 임의의 쓰레기 값
    state = 4

    if nose_confidence > 40:
        # x 좌표값 [0 640] : 100의 자리수로 영역 나누기
        nose_x /= 100
        if (nose_x == 0) or (nose_x == 1) or (nose_x == 2):
            state = 3
        elif nose_x == 3:
            state = 2
        elif (nose_x == 4) or (nose_x == 5) or (nose_x == 6):
            state = 1
    else:
        # 중심에 있는지 판단 어려워도 데이터 계속 보내는게 낫겠죠?
        state = 4
    return state


#print(step_motor(263, 308, 237, 361, 241, 251))
#print(lin2_motor(400, 50))

l = [1,2,3]

a,b,c = map(lambda x: x, l)

print(a,b,c)

