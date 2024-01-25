import threading
import paho.mqtt.publish as publish

import OutputLock
from broker_settings import HOSTNAME, PORT

alarm_batch = []
publish_data_counter = 0
publish_data_limit = 1
counter_lock = threading.Lock()


def publisher_task(event, alarm_batch):
    global publish_data_counter, publish_data_limit
    while True:
        event.wait()
        with counter_lock:
            local_dms_batch = alarm_batch.copy()
            publish_data_counter = 0
            alarm_batch.clear()
        publish.multiple(local_dms_batch, hostname=HOSTNAME, port=PORT)
        with OutputLock.output_lock:
            print(f'published {publish_data_limit} alarm values')
        event.clear()


publish_event = threading.Event()
publisher_thread = threading.Thread(target=publisher_task, args=(publish_event, alarm_batch,))
publisher_thread.daemon = True
publisher_thread.start()