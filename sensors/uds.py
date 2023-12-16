import time

import RPi.GPIO as GPIO

class UDS(object):
    def __init__(self, settings):
        self.TRIG_PIN = settings["TRIG_PIN"]
        self.ECHO_PIN = settings["ECHO_PIN"]
        GPIO.setup(self.TRIG_PIN, GPIO.OUT)
        GPIO.setup(self.ECHO_PIN, GPIO.IN)
    def read_sensor(self):
        GPIO.output(self.TRIG_PIN, False)
        time.sleep(0.2)
        GPIO.output(self.TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG_PIN, False)
        pulse_start_time = time.time()
        pulse_end_time = time.time()

        max_iter = 5000

        iter = 0
        while GPIO.input(self.ECHO_PIN) == 0:
            if iter > max_iter:
                return None
            pulse_start_time = time.time()
            iter += 1

        iter = 0
        while GPIO.input(self.ECHO_PIN) == 1:
            if iter > max_iter:
                return None
            pulse_end_time = time.time()
            iter += 1

        pulse_duration = pulse_end_time - pulse_start_time
        distance = (pulse_duration * 34300) / 2
        return distance

def run_uds_loop(uds, delay, callback, stop_event, device):
    while True:
        callback(uds.read_sensor())
        if stop_event.is_set():
            break
        time.sleep(delay)  # Delay between readings