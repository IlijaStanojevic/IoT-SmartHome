import random
import time


def generate_values(initial_temp=25, initial_humidity=20):
    while True:
        x = 0
        y = 0
        z = 0
        if random.randint(1, 100) < 5:
            x += random.randint(2, 10)
            y += random.randint(2, 10)
            z += random.randint(2, 10)
        yield x, y, z


def run_gsg_simulator(delay, callback, stop_event, settings):
    for x, y, z in generate_values():
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(x, y, z, "GSG_OK", settings)
        if stop_event.is_set():
            break