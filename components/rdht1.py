from OutputLock import OutputLock
from simulators.dht import run_dht_simulator
import threading
import time


def dht_callback(humidity, temperature, code):
    t = time.localtime()
    OutputLock.safe_print("="*20)
    OutputLock.safe_print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    OutputLock.safe_print(f"Code: {code}")
    OutputLock.safe_print(f"Humidity: {humidity}%")
    OutputLock.safe_print(f"Temperature: {temperature}°C")
    OutputLock.safe_print("=" * 20)


def run_rdht1(settings, threads, stop_event):
        if settings['simulated']:
            print("Starting rdth1 sumilator")
            rdht1_thread = threading.Thread(target = run_dht_simulator, args=(2, dht_callback, stop_event))
            rdht1_thread.start()
            threads.append(rdht1_thread)
            print("RDht1 sumilator started")
        else:
            from sensors.dht import run_dht_loop, DHT
            print("Starting rdht1 loop")
            dht = DHT(settings['pin'])
            rdht1_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, dht_callback, stop_event))
            rdht1_thread.start()
            threads.append(rdht1_thread)
            print("RDht1 loop started")
