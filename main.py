import threading

from components.db import run_db
from components.ds1 import run_ds
from components.dus1 import run_uds
from components.dpir1 import run_dpir1
from components.rpir1 import run_rpir1
from components.rpir2 import run_rpir2
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
        dpir1_settings = settings["DPIR1"]
        rpir1_settings = settings["RPIR1"]
        rpir2_settings = settings["RPIR2"]
        dus1_settings = settings['DUS1']
        ds1_settings = settings["DS1"]
        db_settings = settings["DB"]
        run_dht(dht1_settings, threads, stop_event)
        run_dpir1(dpir1_settings, threads, stop_event)
        run_rpir1(rpir1_settings, threads, stop_event)
        run_rpir2(rpir2_settings, threads, stop_event)
        run_uds(dus1_settings, threads, stop_event)
        run_db(db_settings, threads, stop_event)
        run_ds(ds1_settings, threads, stop_event)
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print('Stopping app')
        for t in threads:
            stop_event.set()
