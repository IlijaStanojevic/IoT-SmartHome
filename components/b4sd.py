from OutputLock import output_lock
from simulators.b4sd import run_b4sd_simulator
import threading
import time

def b4sd_callback(time_b4sd, blinking, settings):
    with output_lock:
        print("=" * 20)
        print("Current time on b4sd: " + time_b4sd)
        print("Blinking: " + str(blinking))
        print("Device: " + settings["name"] + " on " + settings["runs_on"])
        print("=" * 20)

def run_b4sd(settings, threads, stop_event, blinking_event):
    if settings['simulated']:
        print("Starting b4sd sumilator")
        b4sd_thread = threading.Thread(target=run_b4sd_simulator, args=(2, b4sd_callback, stop_event, settings, blinking_event))
        b4sd_thread.start()
        threads.append(b4sd_thread)
        print("b4sd simulator started")
    else:
        from actuators.b4sd import run_b4sd_loop, B4SD
        print("Starting b4sd loop")
        b4sd = B4SD(settings)
        b4sd_thread = threading.Thread(target=run_b4sd_loop, args=(b4sd, 2, b4sd_callback, stop_event, settings, blinking_event))
        b4sd_thread.start()
        threads.append(b4sd_thread)
        print("b4sd loop started")