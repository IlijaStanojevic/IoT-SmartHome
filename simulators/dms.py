import json
import time
import random

import Alarm
from OutputLock import output_lock
from daemons import alarmDaemon


def generate_values(settings):
    while True:
        is_pressed = random.choice([0, 100])
        # dms = random.choice(["A", "B", "C", "D", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
        if Alarm.alarm and is_pressed < 70:
            with Alarm.alarm_lock:
                Alarm.alarm = False
                with output_lock:
                    print(f"Alarm: bzzz")
                    alarm_payload = {
                        "measurement": "Alarm",
                        "simulated": settings['simulated'],
                        "runs_on": settings["runs_on"],
                        "name": settings["name"],
                        "value": Alarm.alarm
                    }
                    alarmDaemon.alarm_batch.append((settings["name"], json.dumps(alarm_payload), 0, True))
                    alarmDaemon.publish_data_counter += 1
                    if alarmDaemon.publish_data_counter >= alarmDaemon.publish_data_limit:
                        alarmDaemon.publish_event.set()
                Alarm.alarm_active = False
                Alarm.password = ""
            yield Alarm.password
        elif is_pressed <= 10 and not Alarm.alarm_active:
            for i in range(4):
                dms = random.choice(["A", "B", "C", "D", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
                with Alarm.alarm_lock:
                    Alarm.password += dms
            time.sleep(10)
            Alarm.password = "1234"
            with Alarm.alarm_lock:
                Alarm.alarm_active = True
            yield Alarm.password
        else:
            yield None


def run_dms_simulator(delay, callback, stop_event, settings):
    for d in generate_values(settings):
        time.sleep(delay)
        callback(d, settings)
        if stop_event.is_set():
            break
