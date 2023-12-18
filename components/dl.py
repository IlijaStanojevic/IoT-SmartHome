from OutputLock import output_lock
from components.db import db_callback
import threading
import time

from simulators.led import run_dl_simulator



def dl_callback(is_light_on):
    t = time.localtime()
    if is_light_on == 1:
        with output_lock:
            print("=" * 20)
            print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
            print("Door light is on")
            print("=" * 20)

def run_dl(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting dl simulator")
        dl_thread = threading.Thread(target=run_dl_simulator, args=(2, dl_callback, stop_event))
        dl_thread.start()
        threads.append(dl_thread)
        print("Dl simulator started")
    else:
        from actuators.led import run_led_loop, LED
        print("Starting dl loop")
        led = LED(settings['pin'])
        dl_thread = threading.Thread(target=run_led_loop, args=(led, 2, dl_callback, stop_event))
        dl_thread.start()
        threads.append(dl_thread)
        print("Dl loop started")