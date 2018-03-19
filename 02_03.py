import PRi.GPIO as GPIO
import time
from threading import Timer
LED = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
def q1():
    state = GPIO.LOW
    try:
        while True:
            GPIO.wait_for_edge(LED, GPIO.BOTH)
            if state == GPIO.LOW:
                state = GPIO.HIGH
            else:
                state = GPIO.LOW
            GPIO.output(LED, state)
    except KeyboardInterrupt:
        GPIO.cleanup()

def multi(p, freq):
    p.ChangeFrequency(2 * freq)

def q2():
    freq = 0
    p = GPIO.PWM(LED, freq)
    p.start(50)
    t = None
    try:
        while True:
            GPIO.wait_for_edge(LED, GPIO.BOTH)
            if not t:
                freq = 2
                t = Timer(0.5, multi, [p, freq])
                t.start()
            elif t and t.is_alive():
                t.cancel()
                t = None
                p.ChangeFrequency(0)
                freq = 2
            else:
                t = Timer(0.5, multi, [p, freq])
                freq *= 2
                t.start()
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
