from time import sleep
import serial
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
ser.close()
ser.open()
print(ser.portstr)
ser.flush()


n = 1
try:
    while True:
        ser.write(str(n%255).encode())

        print( str(n%255) + " sended")
        sleep(1)
except KeyboardInterrupt:
    ser.close() 