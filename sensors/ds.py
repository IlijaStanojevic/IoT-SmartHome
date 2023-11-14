import time

import RPi.GPIO as GPIO

class DS(object):
    def __init__(self, pin):
        self.clicked = 0
        self.BUTTON_PIN = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def read_sensor(self):
        def button_clicked():
            self.clicked = 1
        def button_not_clicked():
            self.clicked = 0

        GPIO.add_event_detect(self.BUTTON_PIN, GPIO.RISING, callback=button_clicked, bouncetime=100)
        GPIO.add_event_detect(self.BUTTON_PIN, GPIO.FALLING, callback=button_not_clicked(), bouncetime=100)


def run_ds_loop(ds, delay, callback, stop_event, device):
    while True:
        ds.read_sensor()
        callback(ds.clicked, device)
        if stop_event.is_set():
            break
        time.sleep(delay)  # Delay between readings