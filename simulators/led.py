import time
import random

def generate_values():
    while True:
        yield 1


def run_dl_simulator(delay, callback, stop_event):
    for b in generate_values():
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(b)
        if stop_event.is_set():
            break