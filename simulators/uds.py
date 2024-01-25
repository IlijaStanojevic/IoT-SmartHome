import time
import random

import Alarm

last_4 = [0, 0, 0, 0]


def in_out():
    if last_4[0] + last_4[1] > last_4[2] + last_4[3]:
        Alarm.ppl_num -= 1
    else:
        Alarm.ppl_num += 1


def generate_values(initial_distance=200):
    global last_4
    distance = initial_distance
    person_detected = False
    countdown = 4
    while True:
        # distance = random.randint(1, 200)
        if not person_detected:
            distance = 200
        if person_detected:
            distance = random.randint(1, 50)
            if countdown == 0:
                person_detected = False
            countdown -= 1
            if last_4[0] == 0:
                last_4[0] = distance
            elif last_4[1] == 0:
                last_4[1] = distance
            elif last_4[2] == 0:
                last_4[2] = distance
            else:
                last_4[3] = distance

        elif random.randint(1, 100) <= 10:
            person_detected = True
            countdown = random.randint(1, 3)

        if 0 not in last_4 and Alarm.dpir1_detect:
            in_out()
            last_4 = [0, 0, 0, 0]
            with Alarm.alarm_lock:
                Alarm.dpir1_detect = False
        if 0 not in last_4:
            last_4 = [0, 0, 0, 0]
        yield distance


def run_uds_simulator(delay, callback, stop_event, settings):
    for d in generate_values():
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(d, settings)
        if stop_event.is_set():
            break
