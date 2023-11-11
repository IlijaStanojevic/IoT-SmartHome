import threading
import time

from simulators.dms import run_dms_simulator


def dms_callback(is_pressed):
    if is_pressed:
        print(f"DMS input: {is_pressed}")

def run_dms(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting dms simulator")
        dms_thread = threading.Thread(target=run_dms_simulator, args=(2, dms_callback, stop_event))
        dms_thread.start()
        threads.append(dms_thread)
        print("DMS simulator started")
    else:
        from sensors.dht import run_dht_loop, DHT
        print("Starting rdht1 loop")
        dht = DHT(settings['pin'])
        dht1_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, dms_callback, stop_event))
        dht1_thread.start()
        threads.append(dht1_thread)
        print("RDht1 loop started")
