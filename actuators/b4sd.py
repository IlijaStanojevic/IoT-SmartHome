import RPi.GPIO as GPIO
import time

class B4SD(object):
    def __init__(self, settings):
        self.segments = settings["segments"]
        self.digits = settings["digits"]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.B4SD_PIN, GPIO.IN)
        GPIO.setmode(GPIO.BCM)
        for segment in self.segments:
            GPIO.setup(segment, GPIO.OUT)
            GPIO.output(segment, 0)
        for digit in self.digits:
            GPIO.setup(digit, GPIO.OUT)
            GPIO.output(digit, 1)
        self.num = {' ':(0,0,0,0,0,0,0),
            '0':(1,1,1,1,1,1,0),
            '1':(0,1,1,0,0,0,0),
            '2':(1,1,0,1,1,0,1),
            '3':(1,1,1,1,0,0,1),
            '4':(0,1,1,0,0,1,1),
            '5':(1,0,1,1,0,1,1),
            '6':(1,0,1,1,1,1,1),
            '7':(1,1,1,0,0,0,0),
            '8':(1,1,1,1,1,1,1),
            '9':(1,1,1,1,0,1,1)}
        self.blinking = False
        self.current_time = str(time.ctime()[11:13] + time.ctime()[14:16]).rjust(4)

    def display_current_time(self):
        try:
            while True:
                n = time.ctime()[11:13] + time.ctime()[14:16]
                s = str(n).rjust(4)
                self.current_time = s
                for _ in range(2):
                    for digit in range(4):
                        for loop in range(0, 7):
                            GPIO.output(self.segments[loop], self.num[s[digit]][loop])

                            if self.blinking and (digit == 1) and (int(time.ctime()[18:19]) % 2 == 0):
                                GPIO.output(25, 1)
                            else:
                                GPIO.output(25, 0)

                        GPIO.output(self.digits[digit], 0)
                        time.sleep(0.001)
                        GPIO.output(self.digits[digit], 1)

                    time.sleep(0.5)  # Wait for 0.5 seconds

                if not self.blinking:
                    GPIO.output(25, 0)  # Turn off
                yield s, self.blinking
        finally:
            GPIO.cleanup()
def run_b4sd_loop(b4sd, delay, callback, stop_event, settings, blink_event):
    while True:
        b4sd.display_current_time()
        callback(b4sd.current_time, b4sd.blinking, settings)
        if blink_event.is_set():
            b4sd.blinking = True
        if not blink_event.is_set() and b4sd.blinking:
            b4sd.blinking = False
            blink_event.clear()
        if stop_event.is_set():
            break
        # time.sleep(delay)  # Delay between readings


