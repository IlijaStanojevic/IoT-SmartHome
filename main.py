import threading
import paho.mqtt.client as mqtt
from components.db import run_db
from components.dl import run_dl
from components.dms import run_dms
from components.ds1 import run_ds1
from components.dus1 import run_dus1
from components.dpir1 import run_dpir1
from components.rdht2 import run_rdht2
from components.rdht4 import run_rdht4
from components.rpir1 import run_rpir1
from components.rpir2 import run_rpir2
from components.rpir4 import run_rpir4
from components.b4sd import run_b4sd
from settings import load_settings
from components.rdht1 import run_rdht1
from OutputLock import output_lock
import sys
import time
try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except:
    pass
def on_message(client, userdata, msg):
    if (msg.payload.decode("utf-8") == "TurnOnDL"):
        dl_settings = settings["DL"]
        run_dl(dl_settings, threads, stop_door_light)
        time.sleep(10)
        stop_door_light.set()
    elif (msg.payload.decode("utf-8") == "TurnOnBlinking"):
        blinking_event.set()
        print("Blinking on")
    elif (msg.payload.decode("utf-8") == "TurnOffBlinking"):
        blinking_event.clear()
        print("Blinking off")



def on_connect(client, userdata, flags, rc):
    global current_py
    print("Connected with result code "+str(rc))
    client.subscribe(f"PI{current_py}/commands")

# def user_input_handler(threads, stop_event):
#     dl_settings = settings["DL"]
#     db_settings = settings["DB"]
#     dl_lock = False
#     while True:
#         print("\nMenu:")
#         print("1. Run DB")
#         print("2. Stop DB")
#         print("3. Run DL")
#         print("4. Stop DL")
#         print("0. Exit")
#         choice = input("Enter your choice: ")[0]
#         if choice == '1':
#             stop_buzzer = threading.Event()
#             run_db(db_settings, threads, stop_buzzer)
#         elif choice == '2':
#             stop_buzzer.set()
#         elif choice == '3':
#             stop_door_light = threading.Event()
#             run_dl(dl_settings, threads, stop_door_light)
#         elif choice == '4':
#             stop_door_light.set()
#         elif choice == '0':
#             print('Stopping app')
#             for t in threads:
#                 stop_event.set()
#                 stop_door_light.set()
#                 stop_buzzer.set()
#             break
#         else:
#             print('Invalid choice. Please try again.')
#         time.sleep(0.5)


if __name__ == "__main__":
    print('Starting app')
    if len(sys.argv) != 2:
        print("Format: python main.py py_number")
        print("Ex: python main.py 2")
        print("Using default py 1")
        current_py = 1
    else:
        current_py = int(sys.argv[1])

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60)




    settings = load_settings()
    threads = []
    stop_event = threading.Event()
    stop_buzzer = threading.Event()
    stop_door_light = threading.Event()
    blinking_event = threading.Event()
    try:
        if current_py == 1:
            rdht1_settings = settings['RDHT1']
            rdht2_settings = settings['RDHT2']
            dpir1_settings = settings["DPIR1"]
            rpir1_settings = settings["RPIR1"]
            rpir2_settings = settings["RPIR2"]
            dus1_settings = settings['DUS1']
            ds1_settings = settings["DS1"]
            dms_settings = settings["DMS"]
            run_rdht1(rdht1_settings, threads, stop_event)
            run_rdht2(rdht2_settings, threads, stop_event)
            run_dpir1(dpir1_settings, threads, stop_event)
            run_rpir1(rpir1_settings, threads, stop_event)
            run_rpir2(rpir2_settings, threads, stop_event)
            run_dus1(dus1_settings, threads, stop_event)
            run_ds1(ds1_settings, threads, stop_event)
            run_dms(dms_settings, threads, stop_event)

            # user_input_thread = threading.Thread(target=user_input_handler, args=(threads, stop_event))
            # user_input_thread.start()
        elif current_py == 2:
            pass
        elif current_py == 3:
            rpir4_settings = settings["RPIR4"]
            rdht4_settings = settings['RDHT4']
            bb_settings = settings["BB"]
            b4sd_settings = settings["B4SD"]
            bir_settings = settings["BIR"]
            brgb_settings = settings["BRGB"]
            # run_rpir4(rpir4_settings, threads, stop_event)
            # run_rdht4(rdht4_settings, threads, stop_event)
            run_b4sd(b4sd_settings, threads, stop_event, blinking_event)
        while True:
            client.loop()
            time.sleep(1)

    except KeyboardInterrupt:
        print('Stopping app')
        for t in threads:
            stop_event.set()
        # user_input_thread.join()
