import paho.mqtt.client as mqtt

from OutputLock import output_lock
from simulators.bir import run_bir_simulator
import threading
import time
from broker_settings import *
def bir_callback(bir, settings):
    client = mqtt.Client()
    client.connect(HOSTNAME, PORT, 60)
    with output_lock:
        print("=" * 20)
        print("Current bir: " + str(bir))
        print("Device: " + settings["name"] + " on " + settings["runs_on"])
        if bir in ["OFF", "WHITE", "RED", "GREEN", "BLUE", "YELLOW", "PURPLE", "LIGHT_BLUE"]:
            client.publish("PI3/commands", f"RGB_{bir}")
        print("=" * 20)


def run_bir(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting bir simulator")
        bir_thread = threading.Thread(target=run_bir_simulator, args=(10, bir_callback, stop_event, settings))
        bir_thread.start()
        threads.append(bir_thread)
        print("Bir simulator started")
    else:
        from sensors.bir import run_bir_loop, BIR
        print("Starting bir loop")
        bir = BIR(settings['pin'])
        bir_thread = threading.Thread(target=run_bir_loop, args=(bir, 2, bir_callback, stop_event, settings))
        bir_thread.start()
        threads.append(bir_thread)
        print("Bir loop started")