import json
import time
import random

import Alarm
from OutputLock import output_lock
from daemons import alarmDaemon


def generate_values(settings):
    while True:
        motion = random.random()
        if motion > 0.9:
            if 'RPIR' in settings['name']:
                with Alarm.alarm_lock:
                    Alarm.dpir1_detect = True
                if Alarm.ppl_num == 0 and Alarm.alarm_active:
                    with Alarm.alarm_lock:
                        Alarm.alarm = True
                        with output_lock:
                            print(f"Alarm: bzzz")
                            alarm_payload = {
                                "measurement": "Alarm",
                                "simulated": settings['simulated'],
                                "runs_on": settings["runs_on"],
                                "name": settings["name"],
                                "password": Alarm.password,
                                "value": True
                            }
                            alarmDaemon.alarm_batch.append((settings["name"], json.dumps(alarm_payload), 0, True))
                            alarmDaemon.publish_data_counter += 1
                            if alarmDaemon.publish_data_counter >= alarmDaemon.publish_data_limit:
                                alarmDaemon.publish_event.set()

            yield True
        else:
            yield False


def run_pir_simulator(delay, callback, stop_event, settings):
    for m in generate_values(settings):
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(m, settings)
        if stop_event.is_set():
            break
