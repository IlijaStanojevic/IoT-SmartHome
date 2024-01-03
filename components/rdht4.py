from components.rdht1 import dht_callback
from simulators.dht import run_dht_simulator
import threading
import time





def run_rdht4(settings, threads, stop_event):
        if settings['simulated']:
            print("Starting rdth4 simulator")
            rdht4_thread = threading.Thread(target = run_dht_simulator, args=(2, dht_callback, stop_event, settings))
            rdht4_thread.start()
            threads.append(rdht4_thread)
            print("RDHT4 simulator started")
        else:
            from sensors.dht import run_dht_loop, DHT
            print("Starting rdht4 loop")
            dht = DHT(settings['pin'])
            rdht4_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, dht_callback, stop_event, settings))
            rdht4_thread.start()
            threads.append(rdht4_thread)
            print("RDht4 loop started")
