from OutputLock import output_lock
from components.db import db_callback
from simulators.db import run_db_simulator
import threading
import time

from simulators.led import run_dl_simulator



def dl_callback(is_light_on):
    t = time.localtime()
    if is_light_on == 1:
        print("=" * 20)
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        print("Door light is on")
        print("=" * 20)

def run_dl(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting dl sumilator")
        dpir1_thread = threading.Thread(target=run_dl_simulator, args=(2, dl_callback, stop_event))
        dpir1_thread.start()
        threads.append(dpir1_thread)
        print("Dl simulator started")
    else:
        from sensors.dht import run_dht_loop, DHT
        print("Starting db loop")
        dht = DHT(settings['pin'])
        dpir1_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, db_callback, stop_event))
        dpir1_thread.start()
        threads.append(dpir1_thread)
        print("Db loop started")