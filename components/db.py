from OutputLock import output_lock
from simulators.db import run_db_simulator
import threading
import time

def buzz(pitch, duration):
    period = 1.0 / pitch
    delay = period / 2
    with output_lock:
        print("Started door buzzer")
    time.sleep(delay)
    with output_lock:
        print("Ended door buzzer")


def db_callback(is_buzz):
    t = time.localtime()
    if is_buzz == 1:
        print("=" * 20)
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        # buzz(440, 0.4)
        print("Door buzzing")
        print("=" * 20)

def run_db(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting db sumilator")
        db_thread = threading.Thread(target=run_db_simulator, args=(2, db_callback, stop_event))
        db_thread.start()
        threads.append(db_thread)
        print("Db simulator started")
    else:
        from actuators.db import run_db_loop, Buzzer
        print("Starting db loop")
        buzzer = Buzzer(settings['pin'])
        db_thread = threading.Thread(target=run_db_loop, args=(buzzer, 2, db_callback, stop_event))
        db_thread.start()
        threads.append(db_thread)
        print("Db loop started")