import threading
import time
from simulators.pir import run_pir_simulator
from components.rpir1 import pir_callback
from OutputLock import output_lock

def motion_detected(device):
        print(f"Motion detected at {device}")
def no_motion(device):
        print(f"No motion detected at {device}")




def run_rpir4(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting rpir4 sumilator")
        rpir4_thread = threading.Thread(target=run_pir_simulator, args=(4, pir_callback, stop_event, settings))
        rpir4_thread.start()
        threads.append(rpir4_thread)
        print("Rpir4 simulator started")
    else:
        from sensors.pir import run_pir_loop, PIR
        print("Starting rpir4 loop")
        pir = PIR(settings['pin'])
        rpir4_thread = threading.Thread(target=run_pir_loop, args=(pir, 2, pir_callback, stop_event, settings))
        rpir4_thread.start()
        threads.append(rpir4_thread)
        print("rpir4 loop started")