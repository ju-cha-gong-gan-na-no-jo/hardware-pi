import RPi_I2C_driver
from time import *
mylcd = RPi_I2C_driver.lcd()
mylcd.lcd_display_string("Hello World",1)
mylcd.lcd_display_string("Raspberry Pi3 b+",2)
