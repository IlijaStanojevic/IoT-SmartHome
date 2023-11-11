import threading
import time
from simulators.pir import run_pir_simulator
from OutputLock import output_lock

def motion_detected(device):
    print(f"Motion detected at {device}")
def no_motion(device):
    print(f"No motion detected at {device}")

def pir_callback(motion, device):
    with output_lock:
        # t = time.localtime()
        print("="*20)
        # print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        if motion == 1:
            motion_detected(device)
        else:
            no_motion(device)
        print("=" * 20)


def run_dpir1(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting dpir1 sumilator")
        dpir1_thread = threading.Thread(target=run_pir_simulator, args=(4, pir_callback, stop_event, "dpir1"))
        dpir1_thread.start()
        threads.append(dpir1_thread)
        print("Dpir1 simulator started")
    else:
        from sensors.dht import run_dht_loop, DHT
        print("Starting rdht1 loop")
        dht = DHT(settings['pin'])
        dpir1_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, pir_callback, stop_event, "dpir1"))
        dpir1_thread.start()
        threads.append(dpir1_thread)
        print("RDht1 loop started")