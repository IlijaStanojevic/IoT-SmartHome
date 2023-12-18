import RPi.GPIO as GPIO
import time

class Buzzer(object):
    def __init__(self, pin):
        self.BUZZER_PIN = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.BUZZER_PIN, GPIO.OUT)

    def buzz(self, pitch, duration):
        period = 1.0 / pitch
        delay = period / 2
        cycles = int(duration * pitch)
        for i in range(cycles):
            GPIO.output(self.BUZZER_PIN, True)
            time.sleep(delay)
            GPIO.output(self.BUZZER_PIN, False)
            time.sleep(delay)


def run_db_loop(buzzer, delay, callback, stop_event, settings):
    while True:
        pitch = 440
        duration = 0.3
        buzzer.buzz(pitch, duration)
        callback(1, settings)
        if stop_event.is_set():
            break
        time.sleep(delay)