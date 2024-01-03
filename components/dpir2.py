import threading
import time
from simulators.pir import run_pir_simulator
from OutputLock import output_lock
from components.rpir1 import pir_callback
def motion_detected(device):
    print(f"Motion detected at {device}")
def no_motion(device):
    print(f"No motion detected at {device}")




def run_dpir2(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting dpir2 sumilator")
        dpir2_thread = threading.Thread(target=run_pir_simulator, args=(4, pir_callback, stop_event, settings))
        dpir2_thread.start()
        threads.append(dpir2_thread)
        print("Dpir2 simulator started")
    else:
        from sensors.pir import run_pir_loop, PIR
        print("Starting dpir2 loop")
        pir = PIR(settings['pin'])
        dpir2_thread = threading.Thread(target=run_pir_loop, args=(pir, 2, pir_callback, stop_event, settings))
        dpir2_thread.start()
        threads.append(dpir2_thread)
        print("Dpir2 loop started")