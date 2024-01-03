from components.rdht1 import dht_callback
from simulators.dht import run_dht_simulator
import threading
import time





def run_rdht3(settings, threads, stop_event):
        if settings['simulated']:
            print("Starting rdth3 simulator")
            rdht3_thread = threading.Thread(target = run_dht_simulator, args=(2, dht_callback, stop_event, settings))
            rdht3_thread.start()
            threads.append(rdht3_thread)
            print("RDHT3 simulator started")
        else:
            from sensors.dht import run_dht_loop, DHT
            print("Starting rdht3 loop")
            dht = DHT(settings['pin'])
            rdht3_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, dht_callback, stop_event, settings))
            rdht3_thread.start()
            threads.append(rdht3_thread)
            print("RDht3 loop started")
