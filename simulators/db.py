import time
import random

def generate_values():
    while True:
        buzz = random.choice([0, 1])
        if buzz == 1:
            yield 1
        else:
            yield 0


def run_db_simulator(delay, callback, stop_event):
    for b in generate_values():
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(b)
        if stop_event.is_set():
            break