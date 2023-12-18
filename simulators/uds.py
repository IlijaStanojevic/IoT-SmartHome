import time
import random

def generate_values(initial_distance=200):
    distance = initial_distance
    person_detected = False
    countdown = random.randint(1, 3)
    while True:
        # distance = random.randint(1, 200)
        if not person_detected:
            distance = 200
        if person_detected:
            distance = random.randint(1, 50)
            if countdown == 0:
                person_detected = False
            countdown -= 1
        elif random.randint(1, 100) <= 10:
            person_detected = True
            countdown = random.randint(1, 3)
        yield distance


def run_uds_simulator(delay, callback, stop_event, settings):
    for d in generate_values():
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(d, settings)
        if stop_event.is_set():
            break