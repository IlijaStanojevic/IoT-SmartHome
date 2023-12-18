import json
import threading
import time

from daemons import pirDaemon
from simulators.pir import run_pir_simulator
from OutputLock import output_lock

def motion_detected(device):
    print(f"Motion detected at {device}")
def no_motion(device):
    print(f"No motion detected at {device}")

def pir_callback(motion, settings):
    with output_lock:
        t = time.localtime()
        print("="*20)
        if motion == 1:
            motion_detected(settings["name"])
        else:
            no_motion(settings["name"])
        print("=" * 20)
    pir_payload = {
        "measurement": "Motion",
        "simulated": settings['simulated'],
        "runs_on": settings["runs_on"],
        "name": settings["name"],
        "value": motion
    }
    with output_lock:
        pirDaemon.pir_batch.append((settings["name"], json.dumps(pir_payload), 0, True))
        pirDaemon.publish_data_counter += 1
        if pirDaemon.publish_data_counter >= pirDaemon.publish_data_limit:
            pirDaemon.publish_event.set()

def run_rpir1(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting rpir1 sumilator")
        rpir1_thread = threading.Thread(target=run_pir_simulator, args=(4, pir_callback, stop_event, settings))
        rpir1_thread.start()
        threads.append(rpir1_thread)
        print("Rpir1 simulator started")
    else:
        from sensors.pir import run_pir_loop, PIR
        print("Starting rpir1 loop")
        pir = PIR(settings['pin'])
        rpir1_thread = threading.Thread(target=run_pir_loop, args=(pir, 2, pir_callback, stop_event, settings))
        rpir1_thread.start()
        threads.append(rpir1_thread)
        print("rpir1 loop started")