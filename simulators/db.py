import time
import random




def generate_values():
    period = 1.0 / 440
    delay = period / 2
    while True:
        time.sleep(delay)
        yield 1
        time.sleep(delay)



def run_db_simulator(delay, callback, stop_event):
    for b in generate_values():
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(b)
        if stop_event.is_set():
            break