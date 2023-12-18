import time
import random


def generate_values():
    while True:
        motion = random.choice([0, 1])
        if motion == 1:
            yield True
        else:
            yield False


def run_pir_simulator(delay, callback, stop_event,settings):
    for m in generate_values():
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(m, settings)
        if stop_event.is_set():
            break
