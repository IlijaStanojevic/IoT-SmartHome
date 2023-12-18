import threading
from simulators.ds import run_ds_simulator
from OutputLock import output_lock

def ds_callback(locked, settings):
    if locked:
        with output_lock:
            print("Door is locked")
    else:
        with output_lock:
            print("Door is unlocked")
    ds_payload = {
        "measurement": "Door-sensor",
        "simulated": settings['simulated'],
        "runs_on": settings["runs_on"],
        "name": settings["name"],
        "value": locked
    }
def run_ds(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting ds1 simulator")
        ds1_thread = threading.Thread(target=run_ds_simulator, args=(2, ds_callback, stop_event, settings))
        ds1_thread.start()
        threads.append(ds1_thread)
        print("ds1 simulator started")
    else:
        from sensors.ds import run_ds_loop, DS
        print("Starting ds1 loop")
        dht = DS(settings['pin'])
        ds1_thread = threading.Thread(target=run_ds_loop, args=(dht, 2, ds_callback, stop_event, settings))
        ds1_thread.start()
        threads.append(ds1_thread)
        print("RDht1 loop started")
