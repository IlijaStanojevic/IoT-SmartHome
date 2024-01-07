import time

import RPi.GPIO as GPIO
from time import sleep
class BRGB(object):
    def __init__(self, settings):
        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BCM)

        self.RED_PIN = settings["RED_PIN"]
        self.GREEN_PIN = settings["GREEN_PIN"]
        self.BLUE_PIN = settings["BLUE_PIN"]
        GPIO.setup(self.RED_PIN, GPIO.OUT)
        GPIO.setup(self.GREEN_PIN, GPIO.OUT)
        GPIO.setup(self.BLUE_PIN, GPIO.OUT)
        self.current_color = "OFF"
    def turnOff(self):
        GPIO.output(self.RED_PIN, GPIO.LOW)
        GPIO.output(self.GREEN_PIN, GPIO.LOW)
        GPIO.output(self.BLUE_PIN, GPIO.LOW)
        self.current_color = "OFF"

    def white(self):
        GPIO.output(self.RED_PIN, GPIO.HIGH)
        GPIO.output(self.GREEN_PIN, GPIO.HIGH)
        GPIO.output(self.BLUE_PIN, GPIO.HIGH)
        self.current_color = "WHITE"
    def red(self):
        GPIO.output(self.RED_PIN, GPIO.HIGH)
        GPIO.output(self.GREEN_PIN, GPIO.LOW)
        GPIO.output(self.BLUE_PIN, GPIO.LOW)
        self.current_color = "RED"

    def green(self):
        GPIO.output(self.RED_PIN, GPIO.LOW)
        GPIO.output(self.GREEN_PIN, GPIO.HIGH)
        GPIO.output(self.BLUE_PIN, GPIO.LOW)
        self.current_color = "GREEN"

    def blue(self):
        GPIO.output(self.RED_PIN, GPIO.LOW)
        GPIO.output(self.GREEN_PIN, GPIO.LOW)
        GPIO.output(self.BLUE_PIN, GPIO.HIGH)
        self.current_color = "BLUE"
    def yellow(self):
        GPIO.output(self.RED_PIN, GPIO.HIGH)
        GPIO.output(self.GREEN_PIN, GPIO.HIGH)
        GPIO.output(self.BLUE_PIN, GPIO.LOW)
        self.current_color = "YELLOW"
    def purple(self):
        GPIO.output(self.RED_PIN, GPIO.HIGH)
        GPIO.output(self.GREEN_PIN, GPIO.LOW)
        GPIO.output(self.BLUE_PIN, GPIO.HIGH)
        self.current_color = "PURPLE"
    def lightBlue(self):
        GPIO.output(self.RED_PIN, GPIO.LOW)
        GPIO.output(self.GREEN_PIN, GPIO.HIGH)
        GPIO.output(self.BLUE_PIN, GPIO.HIGH)
        self.current_color = "LIGHT_BLUE"
    def run_loop(self):
        # self.turnOff()
        match self.current_color:
            case "OFF":
                self.turnOff()
            case "WHITE":
                self.white()
            case "RED":
                self.red()
            case "GREEN":
                self.green()
            case "BLUE":
                self.blue()
            case "YELLOW":
                self.yellow()
            case "PURPLE":
                self.purple()
            case "LIGHT_BLUE":
                self.lightBlue()
            case _:
                print(f"Invalid color: {self.current_color}")
                self.current_color = "OFF"
                self.turnOff()

def run_brgb_loop(brgb, delay, callback, brgb_event, settings):
    while True:
        brgb.current_color = brgb_event.color
        time.sleep(0.1)
        brgb_event.clear()
        brgb_event.color = brgb.current_color
        brgb.run_loop()
        callback(brgb.current_color, settings)
        if brgb_event.is_set():
            break