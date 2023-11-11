import threading
class OutputLock:
    lock = threading.Lock()
    @classmethod
    def safe_print(cls, s):
        with cls.lock:
            print(s)