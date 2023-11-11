from OutputLock import output_lock
from simulators.db import run_db_simulator
import threading
import time

def buzz(pitch, duration):
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duration * pitch)
    with output_lock:
        print("Started door buzzer")
    time.sleep(delay)
    with output_lock:
        print("Ended door buzzer")
    time.sleep(delay)


def db_callback(is_buzz):
    t = time.localtime()
    if is_buzz == 1:
        print("=" * 20)
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        buzz(440, 0.4)
        print("=" * 20)

def run_db(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting db sumilator")
        dpir1_thread = threading.Thread(target=run_db_simulator, args=(2, db_callback, stop_event))
        dpir1_thread.start()
        threads.append(dpir1_thread)
        print("Db simulator started")
    else:
        from sensors.dht import run_dht_loop, DHT
        print("Starting db loop")
        dht = DHT(settings['pin'])
        dpir1_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, db_callback, stop_event))
        dpir1_thread.start()
        threads.append(dpir1_thread)
        print("Db loop started")