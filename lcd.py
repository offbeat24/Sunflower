import I2C_LCD_driver
import time
import socket
import os
import RPi.GPIO as GPIO
import serial
import subprocess

mylcd = I2C_LCD_driver.lcd()

ser = serial.Serial('/dev/ttyS0', 115200)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

mylcd.lcd_display_string(f'{s.getsockname()[0]}',1)



mylcd.lcd_display_string("Ready to Activate",2)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
flag = False
while True :
    button_on = GPIO.input(17)
    button_off = GPIO.input(18)
    if (button_on == True) and (flag == False) :
        os.system(ROSSET4)
        ser.write("^^^".encode())
        mylcd.lcd_display_string("",2)
        mylcd.lcd_display_string("Activated",2)
        time.sleep(1)
        flag = True
    elif (button_off == True) and (flag == True) :
        os.system("killall tensor_publisher")
        os.system("killall calculator")
        os.system("killall cmd_selector")
        os.system("killall serial_talker")
        time.sleep(1)
        mylcd.lcd_display_string("",2)
        mylcd.lcd_display_string("Deactivated",2)
        flag = False

GPIO.cleanup()

print ("Button Press Ended")

