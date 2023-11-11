import time
import random


def generate_values():
    while True:
        motion = random.choice([0, 1])
        if motion == 1:
            yield 1
        else:
            yield 0


def run_pir_simulator(delay, callback, stop_event, device):
    for m in generate_values():
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(m, device)
        if stop_event.is_set():
            break
