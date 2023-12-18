import time

import RPi.GPIO as GPIO

class LED(object):
    def __init__(self, pin):
        self.LED_PIN = pin
        self.motion = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED_PIN, GPIO.OUT)
        print(":D")
    def ligth_on(self):
        GPIO.output(self.LED_PIN,GPIO.HIGH)
    def ligth_off(self):
        GPIO.output(self.LED_PIN,GPIO.LOW)


def run_led_loop(led, delay, callback, stop_event, settings):
    while True:
        led.ligth_on()
        callback(1, settings)
        if stop_event.is_set():
            led.ligth_off()
            break
        time.sleep(delay)  # Delay between readings