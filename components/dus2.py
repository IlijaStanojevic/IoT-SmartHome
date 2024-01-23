import json
import threading
import time
from components.dus1 import dus_callback
from daemons import udsDaemon
from simulators.uds import run_uds_simulator
from OutputLock import output_lock



def run_dus2(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting dus2 simulator")
        dus2_thread = threading.Thread(target=run_uds_simulator, args=(2, dus_callback, stop_event, settings))
        dus2_thread.start()
        threads.append(dus2_thread)
        print("dus2 simulator started")
    else:
        from sensors.uds import run_uds_loop, UDS
        print("Starting dus2 loop")
        dht = UDS(settings)
        dus2_thread = threading.Thread(target=run_uds_loop, args=(dht, 2, dus_callback, stop_event, settings))
        dus2_thread.start()
        threads.append(dus2_thread)
        print("Dus2 loop started")
