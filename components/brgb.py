from OutputLock import output_lock

import threading
import time

from simulators.brgb import run_brgb_simulator


def brgb_callback(current_color, settings):
    with output_lock:
        print("=" * 20)
        print("Current color on brgb: " + current_color)
        print("Device: " + settings["name"] + " on " + settings["runs_on"])
        print("=" * 20)


def run_brgb(settings, threads, brgb_event):
    if settings['simulated']:
        print("Starting brgb sumilator")
        brgb_thread = threading.Thread(target=run_brgb_simulator, args=(2, brgb_callback, brgb_event, settings))
        brgb_thread.start()
        threads.append(brgb_thread)
        print("brgb simulator started")
    else:
        from actuators.brgb import run_brgb_loop, BRGB
        print("Starting brgb loop")
        brgb = BRGB(settings)
        brgb_thread = threading.Thread(target=run_brgb_loop, args=(brgb, 2, brgb_callback, brgb_event, settings))
        brgb_thread.start()
        threads.append(brgb_thread)
        print("brgb loop started")