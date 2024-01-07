#!/usr/bin/env python3
import time

from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD

from time import sleep, strftime
from datetime import datetime


class GLCD(object):
    def __init__(self, settings):
        self.PCF8574_address = 0x27
        self.PCF8574A_address = 0x3F
        try:
            self.mcp = PCF8574_GPIO(self.PCF8574_address)
        except:
            try:
                self.mcp = PCF8574_GPIO(self.PCF8574A_address)
            except:
                print('I2C Address Error !')
                exit(1)
        # Create LCD, passing in MCP GPIO adapter.
        self.lcd = Adafruit_CharLCD(pin_rs=settings["pin_rs"], pin_e=settings["pin_e"], pins_db=settings["pins_db"],
                                    GPIO=self.mcp)
        self.temperature = 0
        self.humidity = 0

    def loop(self):
        self.mcp.output(3, 1)  # turn on LCD backlight
        self.lcd.begin(16, 2)  # set number of LCD lines and columns
        while (True):
            # lcd.clear()
            self.lcd.setCursor(0, 0)
            self.lcd.message('Temp: ' + str(self.temperature) + '\n')  # display CPU temperature
            self.lcd.message('Humidity: ' + str(self.humidity))  # display the time
            sleep(1)

    def destroy(self):
        self.lcd.clear()


# def get_cpu_temp():  # get CPU temperature and store it into file "/sys/class/thermal/thermal_zone0/temp"
#     tmp = open('/sys/class/thermal/thermal_zone0/temp')
#     cpu = tmp.read()
#     tmp.close()
#     return '{:.2f}'.format(float(cpu) / 1000) + ' C'
#
#
# def get_time_now():  # get system time
#     return datetime.now().strftime('    %H:%M:%S')
#
#
# def loop():
#     mcp.output(3, 1)  # turn on LCD backlight
#     lcd.begin(16, 2)  # set number of LCD lines and columns
#     while (True):
#         # lcd.clear()
#         lcd.setCursor(0, 0)  # set cursor position
#         lcd.message('CPU: ' + get_cpu_temp() + '\n')  # display CPU temperature
#         lcd.message(get_time_now())  # display the time
#         sleep(1)
#
#
# def destroy():
#     lcd.clear()


# PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
# PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# # Create PCF8574 GPIO adapter.
# try:
# 	mcp = PCF8574_GPIO(PCF8574_address)
# except:
# 	try:
# 		mcp = PCF8574_GPIO(PCF8574A_address)
# 	except:
# 		print ('I2C Address Error !')
# 		exit(1)
# # Create LCD, passing in MCP GPIO adapter.
# lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
def run_glcd_loop(glcd, delay, callback, stop_event, settings):
    while True:
        glcd.loop()
        callback(glcd.temperature, glcd.humidity, settings)
        if stop_event.is_set():
            glcd.destroy()
            break
        time.sleep(delay)  # Delay between readings
