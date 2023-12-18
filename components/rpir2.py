import threading
import time
from simulators.pir import run_pir_simulator
from components.rpir1 import pir_callback
from OutputLock import output_lock

def motion_detected(device):
        print(f"Motion detected at {device}")
def no_motion(device):
        print(f"No motion detected at {device}")




def run_rpir2(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting rpir2 sumilator")
        rpir2_thread = threading.Thread(target=run_pir_simulator, args=(4, pir_callback, stop_event, settings))
        rpir2_thread.start()
        threads.append(rpir2_thread)
        print("Rpir2 simulator started")
    else:
        from sensors.pir import run_pir_loop, PIR
        print("Starting rpir2 loop")
        pir = PIR(settings['pin'])
        rpir2_thread = threading.Thread(target=run_pir_loop, args=(pir, 2, pir_callback, stop_event, settings))
        rpir2_thread.start()
        threads.append(rpir2_thread)
        print("rpir2 loop started")