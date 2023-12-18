import threading
import paho.mqtt.publish as publish

import OutputLock
from broker_settings import HOSTNAME, PORT

pir_batch = []
publish_data_counter = 0
publish_data_limit = 5
counter_lock = threading.Lock()


def publisher_task(event, pir_batch):
    global publish_data_counter, publish_data_limit
    while True:
        event.wait()
        with counter_lock:
            local_dms_batch = pir_batch.copy()
            publish_data_counter = 0
            pir_batch.clear()
        publish.multiple(local_dms_batch, hostname=HOSTNAME, port=PORT)
        with OutputLock.output_lock:
            print(f'published {publish_data_limit} ds values')
        event.clear()


publish_event = threading.Event()
publisher_thread = threading.Thread(target=publisher_task, args=(publish_event, pir_batch,))
publisher_thread.daemon = True
publisher_thread.start()