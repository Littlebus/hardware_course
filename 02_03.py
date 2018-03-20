import RPi.GPIO as GPIO
import time
from threading import Timer
LED = 26
KEY = 20
GPIO.setwarnings(False)
def q1():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED,GPIO.OUT)
    GPIO.setup(KEY, GPIO.IN, GPIO.PUD_UP)
    state = GPIO.LOW
    try:
        while True:
            GPIO.wait_for_edge(KEY, GPIO.FALLING, bouncetime=200)
            if state == GPIO.LOW:
                state = GPIO.HIGH
            else:
                state = GPIO.LOW
            GPIO.output(LED, state)
    except KeyboardInterrupt:
        GPIO.cleanup()

def multi(p, freq):
    p.ChangeFrequency(freq)

def q2():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED,GPIO.OUT)
    GPIO.setup(KEY, GPIO.IN, GPIO.PUD_UP)
    freq = 2
    p = GPIO.PWM(LED, freq)
    t = None
    try:
        while True:
            GPIO.wait_for_edge(KEY, GPIO.RISING, bouncetime=100)
            if not t:
                freq = 2
                p.ChangeFrequency(freq)
                p.start(10)
                t = Timer(0.3, multi, [p, freq])
                t.start()
            elif t and t.is_alive():
                t.cancel()
                t = None
                p.stop()
            else:
                freq *= 2
                t = Timer(0.3, multi, [p, freq])
                t.start()
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
if __name__ == "__main__":
    q1()
    q2()
