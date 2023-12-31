from components.rdht1 import dht_callback
from simulators.dht import run_dht_simulator
import threading
import time





def run_rdht2(settings, threads, stop_event):
        if settings['simulated']:
            print("Starting rdth2 simulator")
            rdht2_thread = threading.Thread(target = run_dht_simulator, args=(2, dht_callback, stop_event, settings))
            rdht2_thread.start()
            threads.append(rdht2_thread)
            print("RDHT2 simulator started")
        else:
            from sensors.dht import run_dht_loop, DHT
            print("Starting rdht2 loop")
            dht = DHT(settings['pin'])
            rdht2_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, dht_callback, stop_event, settings))
            rdht2_thread.start()
            threads.append(rdht2_thread)
            print("RDht2 loop started")
