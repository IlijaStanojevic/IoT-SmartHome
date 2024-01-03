import threading
import time
from simulators.pir import run_pir_simulator
from components.rpir1 import pir_callback
from OutputLock import output_lock

def motion_detected(device):
        print(f"Motion detected at {device}")
def no_motion(device):
        print(f"No motion detected at {device}")




def run_rpir3(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting rpir3 sumilator")
        rpir3_thread = threading.Thread(target=run_pir_simulator, args=(4, pir_callback, stop_event, settings))
        rpir3_thread.start()
        threads.append(rpir3_thread)
        print("Rpir3 simulator started")
    else:
        from sensors.pir import run_pir_loop, PIR
        print("Starting rpir3 loop")
        pir = PIR(settings['pin'])
        rpir3_thread = threading.Thread(target=run_pir_loop, args=(pir, 2, pir_callback, stop_event, settings))
        rpir3_thread.start()
        threads.append(rpir3_thread)
        print("rpir3 loop started")