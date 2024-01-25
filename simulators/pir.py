import time
import random

import Alarm


def generate_values():
    while True:
        motion = random.random()
        if motion > 0.9:
            with Alarm.alarm_lock:
                Alarm.dpir1_detect = True
            if Alarm.ppl_num == 0 and Alarm.alarm_active:
                with Alarm.alarm_lock:
                    Alarm.alarm = True
            yield True
        else:
            yield False


def run_pir_simulator(delay, callback, stop_event, settings):
    for m in generate_values():
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(m, settings)
        if stop_event.is_set():
            break
