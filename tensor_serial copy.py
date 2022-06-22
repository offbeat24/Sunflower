import asyncio
import serial_asyncio
import cv2
import tensorflow as tf
import numpy as np

async def main(loop):
    _, writer = await serial_asyncio.open_serial_connection(url='/dev/ttyS0', baudrate=115200)
    print('Writer created')
    print('connected')
    interpreter = tf.lite.Interpreter(model_path="lite-model_movenet_singlepose_lightning_3.tflite")
    interpreter.allocate_tensors()
    cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
    while cap.isOpened():
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
        keypoints = keypoints_with_scores[:7]
        y, x, _ = frame.shape
        data = list()
        shaped = np.squeeze(np.multiply(keypoints, [y, x, 100]))
        for shape in shaped :
            data += shape.tolist()
        datastr = [f'{int(x)}' for x in data]
        #datastr = ["^"] + datastr + ["_"]
        msg = "*".join(datastr)
        sent = send(writer, msg)
        await asyncio.wait([sent])


async def send(w, msgs):
    for msg in msgs:
        w.write(msg.encode())
        print(f'sent: {msg} in {msgs}')
    print('Done sending')


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()


