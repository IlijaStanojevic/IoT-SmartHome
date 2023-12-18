import threading
import paho.mqtt.publish as publish

import OutputLock
from broker_settings import HOSTNAME, PORT

uds_batch = []
publish_data_counter = 0
publish_data_limit = 5
counter_lock = threading.Lock()


def publisher_task(event, uds_batch):
    global publish_data_counter, publish_data_limit
    while True:
        event.wait()
        with counter_lock:
            local_dms_batch = uds_batch.copy()
            publish_data_counter = 0
            uds_batch.clear()
        publish.multiple(local_dms_batch, hostname=HOSTNAME, port=PORT)
        with OutputLock.output_lock:
            print(f'published {publish_data_limit} uds values')
        event.clear()


publish_event = threading.Event()
publisher_thread = threading.Thread(target=publisher_task, args=(publish_event, uds_batch,))
publisher_thread.daemon = True
publisher_thread.start()