from OutputLock import output_lock

import threading
import time

from simulators.lcd import run_glcd_simulator


def glcd_callback(temperature, humidity, settings):
    with output_lock:
        print("=" * 20)
        print("Display on glcd: " + f"Temp: {temperature}\nHumidity: {humidity}")
        print("Device: " + settings["name"] + " on " + settings["runs_on"])
        print("=" * 20)


def run_glcd(settings, threads, stop_event, lcd_event):
    if settings['simulated']:
        print("Starting glcd simulator")
        glcd_thread = threading.Thread(target=run_glcd_simulator, args=(2, glcd_callback, stop_event, settings, lcd_event))
        glcd_thread.start()
        threads.append(glcd_thread)
        print("glcd simulator started")
    else:
        from actuators.lcd.glcd import run_glcd_loop, GLCD
        print("Starting glcd loop")
        glcd = GLCD(settings)
        glcd_thread = threading.Thread(target=run_glcd_loop, args=(glcd, 2, glcd_callback, stop_event, settings, lcd_event))
        glcd_thread.start()
        threads.append(glcd_thread)
        print("glcd loop started")