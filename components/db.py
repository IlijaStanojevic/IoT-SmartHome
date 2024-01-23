from OutputLock import output_lock
from simulators.db import run_db_simulator
import threading
import time

def db_callback(is_buzz, settings):
    t = time.localtime()
    if is_buzz == 1:
        with output_lock:
            print("=" * 20)
            print("Buzzing")
            print("Device: " + settings["name"] + " on " + settings["runs_on"])
            print("=" * 20)

def run_db(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting db sumilator")
        db_thread = threading.Thread(target=run_db_simulator, args=(2, db_callback, stop_event, settings))
        db_thread.start()
        threads.append(db_thread)
        print("Db simulator started")
    else:
        from actuators.db import run_db_loop, Buzzer
        print("Starting db loop")
        buzzer = Buzzer(settings['pin'])
        db_thread = threading.Thread(target=run_db_loop, args=(buzzer, 2, db_callback, stop_event, settings))
        db_thread.start()
        threads.append(db_thread)
        print("Db loop started")