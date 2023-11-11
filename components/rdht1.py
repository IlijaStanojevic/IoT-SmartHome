from simulators.dht import run_dht_simulator
import threading
import time
from OutputLock import output_lock

def dht_callback(humidity, temperature, code, device):
    with output_lock:
        # t = time.localtime()
        print("="*20)
        # print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        # print(f"Code: {code}")
        print(f"Device: {device}")
        print(f"Humidity: {humidity}%")
        print(f"Temperature: {temperature}°C")
        print("=" * 20)


def run_rdht1(settings, threads, stop_event):
        if settings['simulated']:
            print("Starting rdth1 simulator")
            rdht1_thread = threading.Thread(target = run_dht_simulator, args=(2, dht_callback, stop_event, "RDHT1"))
            rdht1_thread.start()
            threads.append(rdht1_thread)
            print("RDht1 simulator started")
        else:
            from sensors.dht import run_dht_loop, DHT
            print("Starting rdht1 loop")
            dht = DHT(settings['pin'])
            rdht1_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, dht_callback, stop_event))
            rdht1_thread.start()
            threads.append(rdht1_thread)
            print("RDht1 loop started")
