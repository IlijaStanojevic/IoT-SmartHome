import threading
import time
from simulators.pir import run_pir_simulator
from OutputLock import output_lock

def motion_detected(device):
    with output_lock:
        print(f"Motion detected at {device}")
def no_motion(device):
    with output_lock:
        print(f"No motion detected at {device}")

def pir_callback(motion, device):
    with output_lock:
        t = time.localtime()
        print("="*20)
        if motion == 1:
            motion_detected(device)
        else:
            no_motion(device)
        print("=" * 20)


def run_rpir2(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting rpir2 sumilator")
        rpir2_thread = threading.Thread(target=run_pir_simulator, args=(4, pir_callback, stop_event, "rpir2"))
        rpir2_thread.start()
        threads.append(rpir2_thread)
        print("Rpir2 simulator started")
    else:
        from sensors.pir import run_pir_loop, PIR
        print("Starting rpir2 loop")
        pir = PIR(settings['pin'])
        rpir2_thread = threading.Thread(target=run_pir_loop, args=(pir, 2, pir_callback, stop_event, "rpir2"))
        rpir2_thread.start()
        threads.append(rpir2_thread)
        print("rpir2 loop started")