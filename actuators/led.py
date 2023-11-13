import time

import RPi.GPIO as GPIO

class LED(object):
    def __init__(self, pin):
        self.LED_PIN = pin
        self.motion = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED_PIN, GPIO.IN)
    def ligth_on(self):
        GPIO.output(self.LED_PIN,GPIO.HIGH)


def run_led_loop(led, delay, callback, stop_event):
    while True:
        led.ligth_on()
        callback(1)
        if stop_event.is_set():
            break
        time.sleep(delay)  # Delay between readings