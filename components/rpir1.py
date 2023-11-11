import threading
import time

from OutputLock import OutputLock
from simulators.pir import run_pir_simulator


def motion_detected(device):
    OutputLock.safe_print(f"Motion detected at {device}")
def no_motion(device):
    OutputLock.safe_print(f"No motion detected at {device}")

def pir_callback(motion, device):
    t = time.localtime()
    print("="*20)
    print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    if motion == 1:
        motion_detected(device)
    else:
        no_motion(device)
    print("=" * 20)


def run_rpir1(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting rpir1 sumilator")
        rpir1_thread = threading.Thread(target=run_pir_simulator, args=(4, pir_callback, stop_event, "rpir1"))
        rpir1_thread.start()
        threads.append(rpir1_thread)
        print("Rpir1 simulator started")
    else:
        from sensors.dht import run_dht_loop, DHT
        print("Starting rdht1 loop")
        dht = DHT(settings['pin'])
        rpir1_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, pir_callback, stop_event))
        rpir1_thread.start()
        threads.append(rpir1_thread)
        print("RDht1 loop started")