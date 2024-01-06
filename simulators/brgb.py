import time

def generate_values(color):
    while True:
        yield color

def run_brgb_simulator(delay, callback, stop_event, settings, color):
    for c in generate_values(color):
        time.sleep(delay)
        callback(c, settings)
        if stop_event.is_set():
            break
