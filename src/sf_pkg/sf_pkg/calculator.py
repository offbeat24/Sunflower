import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
import math

class Calculator(Node) :
    def __init__(self):
        super().__init__('calculator')
        qos_profile = QoSProfile(depth=10)
        self.calculator = self.create_publisher(
            String,
            'tf_command',
            qos_profile)
        self.tflite_subscriber = self.create_subscription(
            String,
            'tflite_result',
            self.calculate_command,
            qos_profile)

    def publish_command(self, cmd) :
        msg = String()
        msg.data = cmd
        self.calculator.publish(msg)
        self.get_logger().info('Published message: {0}'.format(msg.data))

    def calculate_command(self, msg):
        tensor = msg.data.split('*')
        cmd = 0
        cmd += self.lin2_motor(tensor[:3])
        cmd += self.step_motor(tensor[:9])
        cmd += self.eye_dist(tensor[3:9])
        self.publish_command( "*" + f'{cmd}')

    def step_motor(self, tensor):
        n_x, n_y, n_con, l_x, l_y, l_con, r_x, r_y, r_con = map(lambda x: int(x), tensor)
        if (n_con > 40) and (l_con > 40) and (r_con > 40):
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
        return int(theta) * 1000
    
    # 코의 x좌표로 프레임상 얼굴 중심 찾기
    def lin2_motor(self, nose):
        _ , nose_x, nose_confidence = map(lambda x: int(x), nose)
        # 리니어 모터 작동 mode : 1,2,3
        # 임의의 쓰레기 값
        state = 4
        if nose_confidence > 40:
            # x 좌표값 [0 640] : 100의 자리수로 영역 나누기
            nose_x //= 100
            if (nose_x == 0) or (nose_x == 1) or (nose_x == 2):
                state = 3
            elif nose_x == 3:
                state = 2
            elif (nose_x == 4) or (nose_x == 5) or (nose_x == 6):
                state = 1
        else:
            # 중심에 있는지 판단 어려워도 데이터 계속 보내는게 낫겠죠?
            state = 4
        return state*1000000
    
    def eye_dist(self, eye) :
        l_x, l_y, l_c, r_x, r_y, r_c = map(lambda x : int(x), eye)
        if (l_c > 0.4) and (r_c > 0.4):
        # length를 float으로 보내도 되쥬?
            length = ((l_x - r_x) ** 2 + (l_y - r_y) ** 2) ** (1 / 2)
        else :
            length = 999
        return int(length)

def main(args=None) :
    rclpy.init(args=args)
    node = Calculator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__' :
    main()