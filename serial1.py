from time import sleep
import serial
ser = serial.Serial('/dev/ttyS0', 115200, timeout = 1)
ser.close()
ser.open()
print(ser.portstr)
ser.flush()


n = 0
msg = "fuckyou"
try:
    while True:
        for c in msg :
            ser.write(c.encode())
        # print(ser.read())
except KeyboardInterrupt:
    ser.close() 