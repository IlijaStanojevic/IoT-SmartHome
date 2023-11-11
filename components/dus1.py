import threading
import time
from simulators.uds import run_uds_simulator
from OutputLock import output_lock

def uds_callback(distance):
    with output_lock:
        print(f"Distance: {distance}cm")

def run_uds(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting dus1 sumilator")
        dus1_thread = threading.Thread(target=run_uds_simulator, args=(2, uds_callback, stop_event))
        dus1_thread.start()
        threads.append(dus1_thread)
        print("dus1 sumilator started")
    else:
        from sensors.dht import run_dht_loop, DHT
        print("Starting rdht1 loop")
        dht = DHT(settings['pin'])
        dht1_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, uds_callback, stop_event))
        dht1_thread.start()
        threads.append(dht1_thread)
        print("RDht1 loop started")
