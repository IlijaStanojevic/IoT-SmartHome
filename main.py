import threading

from components.dus1 import run_uds
from settings import load_settings
from components.rdht1 import run_dht
import time

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except:
    pass


if __name__ == "__main__":
    print('Starting app')
    settings = load_settings()
    threads = []
    stop_event = threading.Event()
    try:
        dht1_settings = settings['DHT1']
        run_dht(dht1_settings, threads, stop_event)
        dus1_settings = settings['DUS1']
        run_uds(dus1_settings, threads, stop_event)
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print('Stopping app')
        for t in threads:
            stop_event.set()
