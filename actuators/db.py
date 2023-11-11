import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
buzzer_pin = 17
GPIO.setup(buzzer_pin, GPIO.OUT)
def buzz(pitch, duration):
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duration * pitch)
    for i in range(cycles):
        GPIO.output(buzzer_pin, True)
    time.sleep(delay)
    GPIO.output(buzzer_pin, False)
    time.sleep(delay)