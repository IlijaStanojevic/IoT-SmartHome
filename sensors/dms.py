import time

import RPi.GPIO as GPIO

class DMS(object):
    def __init__(self, settings):
        self.R1 = settings["pin_R1"]
        self.R2 = settings["pin_R2"]
        self.R3 = settings["pin_R3"]
        self.R4 = settings["pin_R4"]
        self.C1 = settings["pin_C1"]
        self.C2 = settings["pin_C2"]
        self.C3 = settings["pin_C3"]
        self.C4 = settings["pin_C4"]
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.R1, GPIO.OUT)
        GPIO.setup(self.R2, GPIO.OUT)
        GPIO.setup(self.R3, GPIO.OUT)
        GPIO.setup(self.R4, GPIO.OUT)

        GPIO.setup(self.C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.input = ""

    def readLine(self, line, characters):
        GPIO.output(line, GPIO.HIGH)
        if (GPIO.input(self.C1) == 1):
            self.input = characters[0]
        if (GPIO.input(self.C2) == 1):
            self.input = characters[1]
        if (GPIO.input(self.C3) == 1):
            self.input = characters[2]
        if (GPIO.input(self.C4) == 1):
            self.input = characters[3]
        GPIO.output(line, GPIO.LOW)
    def read_input(self):
        self.readLine(self.R1, ["1", "2", "3", "A"])
        self.readLine(self.R2, ["4", "5", "6", "B"])
        self.readLine(self.R3, ["7", "8", "9", "C"])
        self.readLine(self.R4, ["*", "0", "#", "D"])







def run_dms_loop(dms, delay, callback, stop_event):
    while True:
        dms.read_input()
        callback(dms.input)
        if stop_event.is_set():
            break
        time.sleep(delay)  # Delay between readings