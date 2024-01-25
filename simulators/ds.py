import json
import time
import random

import Alarm
from OutputLock import output_lock
from daemons import alarmDaemon


def generate_values(settings):
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
        if locked:
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
        if not locked and Alarm.alarm_active:
            with Alarm.alarm_lock:
                Alarm.alarm = True
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
        yield locked


def run_ds_simulator(delay, callback, stop_event, settings):
    for d in generate_values(settings):
        time.sleep(delay)
        callback(d, settings)
        if stop_event.is_set():
            break
