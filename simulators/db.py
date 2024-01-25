import time
import random

import Alarm


def generate_values():
    period = 1.0 / 440
    delay = period / 2
    while True:
        time.sleep(delay)
        yield 1
        time.sleep(delay)



def run_db_simulator(delay, callback, stop_event, settings):
    for b in generate_values():
        send = 0
        time.sleep(delay)  # Delay between readings (adjust as needed)
        if Alarm.alarm:
            send = 1
        callback(send, settings)
        if stop_event.is_set():
            break