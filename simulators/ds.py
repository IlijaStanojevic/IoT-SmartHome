import time
import random

import Alarm


def generate_values():
    countdown = random.randint(1, 6)
    temp = countdown
    locked = True
    while True:
        if countdown != 0:
            countdown -= 1
        elif random.randint(1, 100) < 50:
            locked = False
            countdown = random.randint(1, 6)
            temp = countdown
        else:
            locked = True
            countdown = random.randint(1, 6)
            temp = countdown
        if temp >= 5 and not locked:
            with Alarm.alarm_lock:
                Alarm.alarm = True
        if locked:
            with Alarm.alarm_lock:
                Alarm.alarm = False
        if not locked and Alarm.alarm_active:
            with Alarm.alarm_lock:
                Alarm.alarm = True
        yield locked


def run_ds_simulator(delay, callback, stop_event, settings):
    for d in generate_values():
        time.sleep(delay)
        callback(d, settings)
        if stop_event.is_set():
            break
