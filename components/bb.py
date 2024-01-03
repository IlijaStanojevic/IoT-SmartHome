from OutputLock import output_lock
from simulators.db import run_db_simulator
import threading
import time
from db import db_callback


def run_bb(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting bb sumilator")
        bb_thread = threading.Thread(target=run_db_simulator, args=(2, db_callback, stop_event, settings))
        bb_thread.start()
        threads.append(bb_thread)
        print("Bb simulator started")
    else:
        from actuators.db import run_db_loop, Buzzer
        print("Starting bb loop")
        buzzer = Buzzer(settings['pin'])
        bb_thread = threading.Thread(target=run_db_loop, args=(buzzer, 2, db_callback, stop_event, settings))
        bb_thread.start()
        threads.append(bb_thread)
        print("Bb loop started")