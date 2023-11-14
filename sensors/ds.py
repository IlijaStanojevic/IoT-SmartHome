import time

import RPi.GPIO as GPIO

class DS(object):
    def __init__(self, pin):
        self.PIN = pin
        self.motion = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN, GPIO.IN)
    def read_sensor(self):
        def motion_detected(channel):
            self.motion = 1
        def no_motion(channel):
            self.motion = 0
        GPIO.add_event_detect(self.PIR_PIN, GPIO.RISING, callback=motion_detected)
        GPIO.add_event_detect(self.PIR_PIN, GPIO.FALLING, callback=no_motion)

def run_ds_loop(pir, delay, callback, stop_event, device):
    while True:
        pir.read_sensor()
        callback(pir.motion, device)
        if stop_event.is_set():
            break
        time.sleep(delay)  # Delay between readings