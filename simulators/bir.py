import time
import random


def generate_values():
    while True:
        bir = random.choice(["LEFT", "RIGHT", "UP", "DOWN", "RED", "GREEN", "WHITE", "OK", "BLUE", "YELLOW", "PURPLE", "LIGHT_BLUE", "8", "9", "*", "OFF","#"])
        yield bir


def run_bir_simulator(delay, callback, stop_event,settings):
    for b in generate_values():
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(b, settings)
        if stop_event.is_set():
            break
