import time
from pad4pi import rpi_gpio

KEYPAD = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ["*", 0, "#", "&"]
]

ROW_PINS = [19, 26, 20, 21] # BCM numbering #노초파보
COL_PINS = [16, 13, 12, 6] # BCM numbering #회흰빨주

factory = rpi_gpio.KeypadFactory()

# Try factory.create_4_by_3_keypad
# and factory.create_4_by_4_keypad for reasonable defaults
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

def printKey(key):
    print(key)

# printKey will be called each time a keypad button is pressed


try:
    keypad.registerKeyPressHandler(printKey)
    print("gogo")
    while(True):
        time.sleep(0.2)
except:
    keypad.cleanup()
