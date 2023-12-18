import time

import RPi.GPIO as GPIO

class PIR(object):
    def __init__(self, pin):
        self.PIR_PIN = pin
        self.motion = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIR_PIN, GPIO.IN)
    def read_sensor(self):
        def motion_detected(channel):
            self.motion = True
        def no_motion(channel):
            self.motion = False
        GPIO.add_event_detect(self.PIR_PIN, GPIO.RISING, callback=motion_detected)
        GPIO.add_event_detect(self.PIR_PIN, GPIO.FALLING, callback=no_motion)


def run_pir_loop(pir, delay, callback, stop_event, settings):
    while True:
        pir.read_sensor()
        callback(pir.motion, settings)
        if stop_event.is_set():
            break
        time.sleep(delay)  # Delay between readings