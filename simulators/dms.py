import time
import random

def generate_values():
    while True:
        is_pressed = random.choice([0, 1])
        dms = random.choice(["A", "B", "C", "D", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
        if is_pressed == 1:
            yield dms
        else:
            yield None
def run_dms_simulator(delay, callback, stop_event):
    for d in generate_values():
        time.sleep(delay)
        callback(d)
        if stop_event.is_set():
            break