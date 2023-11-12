import threading

from components.db import run_db
from components.dl import run_dl
from components.dms import run_dms
from components.ds1 import run_ds
from components.dus1 import run_uds
from components.dpir1 import run_dpir1
from components.rdht2 import run_rdht2
from components.rpir1 import run_rpir1
from components.rpir2 import run_rpir2
from settings import load_settings
from components.rdht1 import run_rdht1
from OutputLock import output_lock
import time

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except:
    pass

def user_input_handler(threads, stop_event):
    while True:
        print("\nMenu:")
        print("1. Run DB")
        print("2. Stop DB")
        print("3. Run DL")
        print("4. Stop DL")
        print("0. Exit")
        choice = input("Enter your choice: ")[0]
        if choice == '1':
            stop_buzzer = threading.Event()
            run_db(db_settings, threads, stop_buzzer)
        elif choice == '2':
            stop_buzzer.set()
        elif choice == '3':
            stop_door_light = threading.Event()
            run_dl(dms_settings, threads, stop_door_light)
        elif choice == '4':
            stop_door_light.set()
        elif choice == '0':
            print('Stopping app')
            for t in threads:
                stop_event.set()
                stop_door_light.set()
                stop_buzzer.set()
            break
        else:
            print('Invalid choice. Please try again.')
        time.sleep(0.5)


if __name__ == "__main__":
    print('Starting app')
    settings = load_settings()
    threads = []
    stop_event = threading.Event()
    stop_buzzer = threading.Event()
    stop_door_light = threading.Event()
    try:
        rdht1_settings = settings['RDHT1']
        rdht2_settings = settings['RDHT2']
        dpir1_settings = settings["DPIR1"]
        rpir1_settings = settings["RPIR1"]
        rpir2_settings = settings["RPIR2"]
        dus1_settings = settings['DUS1']
        ds1_settings = settings["DS1"]
        db_settings = settings["DB"]
        dms_settings = settings["DMS"]
        run_rdht1(rdht1_settings, threads, stop_event)
        run_rdht2(rdht2_settings, threads, stop_event)
        run_dpir1(dpir1_settings, threads, stop_event)
        run_rpir1(rpir1_settings, threads, stop_event)
        run_rpir2(rpir2_settings, threads, stop_event)
        run_uds(dus1_settings, threads, stop_event)
        # run_db(db_settings, threads, stop_event)
        run_ds(ds1_settings, threads, stop_event)
        run_dms(dms_settings, threads, stop_event)

        user_input_thread = threading.Thread(target=user_input_handler, args=(threads, stop_event))
        user_input_thread.start()
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print('Stopping app')
        for t in threads:
            stop_event.set()
        user_input_thread.join()
