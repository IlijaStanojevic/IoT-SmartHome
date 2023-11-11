import threading
from simulators.ds import run_ds_simulator
from OutputLock import OutputLock

def ds_callback(locked):
    if locked:
        OutputLock.safe_print("Door is locked")
    else:
        OutputLock.safe_print("Door is unlocked")

def run_ds(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting ds1 simulator")
        ds1_thread = threading.Thread(target=run_ds_simulator, args=(2, ds_callback, stop_event))
        ds1_thread.start()
        threads.append(ds1_thread)
        print("ds1 simulator started")
    else:
        from sensors.dht import run_dht_loop, DHT
        print("Starting rdht1 loop")
        dht = DHT(settings['pin'])
        dht1_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, ds_callback, stop_event))
        dht1_thread.start()
        threads.append(dht1_thread)
        print("RDht1 loop started")
