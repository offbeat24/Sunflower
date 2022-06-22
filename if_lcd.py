#!/usr/bin/python3

import I2C_LCD_driver
from time import *
import socket

mylcd = I2C_LCD_driver.lcd()



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

mylcd.lcd_clear()
mylcd.lcd_display_string(f'{s.getsockname()[0]}',1)
mylcd.lcd_display_string("Sunflower",2)


