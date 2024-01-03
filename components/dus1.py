import json
import threading
import time

from daemons import udsDaemon
from simulators.uds import run_uds_simulator
from OutputLock import output_lock

def dus_callback(distance, settings):
    with output_lock:
        print(f"Distance: {distance}cm")
    uds_payload = {
        "measurement": "Distance",
        "simulated": settings['simulated'],
        "runs_on": settings["runs_on"],
        "name": settings["name"],
        "value": distance
    }
    with output_lock:
        udsDaemon.uds_batch.append((settings["name"], json.dumps(uds_payload), 0, True))
        udsDaemon.publish_data_counter += 1
        if udsDaemon.publish_data_counter >= udsDaemon.publish_data_limit:
            udsDaemon.publish_event.set()

def run_dus1(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting dus1 sumilator")
        dus1_thread = threading.Thread(target=run_uds_simulator, args=(2, dus_callback, stop_event, settings))
        dus1_thread.start()
        threads.append(dus1_thread)
        print("dus1 sumilator started")
    else:
        from sensors.uds import run_uds_loop, UDS
        print("Starting dus1 loop")
        dht = UDS(settings)
        dus1_thread = threading.Thread(target=run_uds_loop, args=(dht, 2, dus_callback, stop_event, settings))
        dus1_thread.start()
        threads.append(dus1_thread)
        print("Dus1 loop started")
