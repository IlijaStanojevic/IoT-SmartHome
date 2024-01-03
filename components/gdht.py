from components.rdht1 import dht_callback
from simulators.dht import run_dht_simulator
import threading
import time





def run_gdht(settings, threads, stop_event):
        if settings['simulated']:
            print("Starting gdth simulator")
            gdht_thread = threading.Thread(target = run_dht_simulator, args=(2, dht_callback, stop_event, settings))
            gdht_thread.start()
            threads.append(gdht_thread)
            print("GDHT simulator started")
        else:
            from sensors.dht import run_dht_loop, DHT
            print("Starting gdht loop")
            dht = DHT(settings['pin'])
            gdht_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, dht_callback, stop_event, settings))
            gdht_thread.start()
            threads.append(gdht_thread)
            print("GDHT loop started")
