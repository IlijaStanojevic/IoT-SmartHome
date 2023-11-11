import time
import random

def generate_values():
    countdown = random.randint(1, 4)
    locked = True
    while True:
        if countdown != 0:
            countdown -= 1
        elif random.randint(1, 100) < 50:
            locked = False
            countdown = random.randint(1, 4)
        else:
            locked = True
            countdown = random.randint(1, 4)
        yield locked
def run_ds_simulator(delay, callback, stop_event):
    for d in generate_values():
        time.sleep(delay)
        callback(d)
        if stop_event.is_set():
            break