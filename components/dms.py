import threading
import time

from OutputLock import output_lock
from daemons import dmsDaemon
from simulators.dms import run_dms_simulator


def dms_callback(input, settings):
    if input:

        with output_lock:
            print(f"DMS input: {input}")
            dms_payload = {
                "measurement": "Membrane-switch",
                "simulated": settings['simulated'],
                "runs_on": settings["runs_on"],
                "name": settings["name"],
                "value": input
            }
            dmsDaemon.dms_batch.append(dms_payload)
def run_dms(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting dms simulator")
        dms_thread = threading.Thread(target=run_dms_simulator, args=(2, dms_callback, stop_event, settings))
        dms_thread.start()
        threads.append(dms_thread)
        print("DMS simulator started")
    else:
        from sensors.dms import run_dms_loop, DMS
        print("Starting dms loop")
        dms = DMS(settings)
        dht1_thread = threading.Thread(target=run_dms_loop, args=(dms, 2, dms_callback, stop_event, settings))
        dht1_thread.start()
        threads.append(dht1_thread)
        print("Dms loop started")
