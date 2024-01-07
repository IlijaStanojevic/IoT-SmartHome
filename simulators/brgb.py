import time

def generate_values(brgb_event):
    while True:
        color = brgb_event.color
        time.sleep(0.1)
        brgb_event.clear()
        brgb_event.color = color
        yield color

def run_brgb_simulator(delay, callback, brgb_event, settings):
    for c in generate_values(brgb_event):
        time.sleep(delay)
        callback(c, settings)
        if brgb_event.is_set():
            break
