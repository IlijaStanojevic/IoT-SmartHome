import time
import random

def generate_values(glcd_event):
    while True:
        temperature = glcd_event.temperature
        humidity = glcd_event.humidity
        time.sleep(0.1)
        glcd_event.clear()
        glcd_event.temperature = temperature
        glcd_event.humidity = humidity
        yield temperature, humidity


def run_glcd_simulator(delay, callback, stop_event, settings, glcd_event):
    for t, h in generate_values(glcd_event):
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(t, h, settings)
        if stop_event.is_set():
            break



