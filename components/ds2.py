import json
import threading
from components.ds1 import ds_callback
from daemons import dsDaemon
from simulators.ds import run_ds_simulator
from OutputLock import output_lock



def run_ds2(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting ds2 simulator")
        ds2_thread = threading.Thread(target=run_ds_simulator, args=(15, ds_callback, stop_event, settings))
        ds2_thread.start()
        threads.append(ds2_thread)
        print("ds2 simulator started")
    else:
        from sensors.ds import run_ds_loop, DS
        print("Starting ds2 loop")
        dht = DS(settings['pin'])
        ds2_thread = threading.Thread(target=run_ds_loop, args=(dht, 2, ds_callback, stop_event, settings))
        ds2_thread.start()
        threads.append(ds2_thread)
        print("ds2 loop started")
