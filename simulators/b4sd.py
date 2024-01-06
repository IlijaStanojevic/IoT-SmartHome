import time


def generate_values():
    while True:
        yield str(time.ctime()[11:13] + time.ctime()[14:16]).rjust(4)

def run_b4sd_simulator(delay, callback, stop_event, settings, blink_event):
    for t in generate_values():
        time.sleep(delay)
        callback(t, blink_event.is_set(), settings)
        if stop_event.is_set():
            break
