import json
import threading

import Alarm
from OutputLock import output_lock
from daemons import gsgDaemon, alarmDaemon
from simulators.gsg import run_gsg_simulator


def dht_callback(x, y, z, code, settings):
    if x != 1.5 or y != 1.5 or z!=1.5:
        with Alarm.alarm_lock:
            Alarm.alarm = True
            Alarm.alarm_active = True
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

    with output_lock:
        # t = time.localtime()
        print("="*20)
        # print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        # print(f"Code: {code}")
        print(f"Device:" + settings["name"])
        print(f"X: {x}")
        print(f"Y: {y}")
        print(f"Z: {z}")
        print("=" * 20)

    x_payload = {
        "measurement": "X",
        "simulated": settings['simulated'],
        "runs_on": settings["runs_on"],
        "name": settings["name"],
        "value": x
    }
    y_payload = {
        "measurement": "Y",
        "simulated": settings['simulated'],
        "runs_on": settings["runs_on"],
        "name": settings["name"],
        "value": y
    }
    z_payload = {
        "measurement": "Z",
        "simulated": settings['simulated'],
        "runs_on": settings["runs_on"],
        "name": settings["name"],
        "value": z
    }
    with output_lock:
        gsgDaemon.gsg_batch.append((settings["name"], json.dumps(x_payload), 0, True))
        gsgDaemon.gsg_batch.append((settings["name"], json.dumps(y_payload), 0, True))
        gsgDaemon.gsg_batch.append((settings["name"], json.dumps(z_payload), 0, True))
        gsgDaemon.publish_data_counter += 1
        if gsgDaemon.publish_data_counter >= gsgDaemon.publish_data_limit:
            gsgDaemon.publish_event.set()


def run_gsg(settings, threads, stop_event):
        if settings['simulated']:
            print("Starting rdth1 simulator")
            gsg_thread = threading.Thread(target = run_gsg_simulator, args=(2, dht_callback, stop_event, settings))
            gsg_thread.start()
            threads.append(gsg_thread)
            print("RDht1 simulator started")
        else:
            from sensors.gyro import loop, DHT
            print("Starting rdht1 loop")
            dht = DHT(settings['pin'])
            gsg_thread = threading.Thread(target=loop(), args=(dht, 2, dht_callback, stop_event, settings))
            gsg_thread.start()
            threads.append(gsg_thread)
            print("RDht1 loop started")