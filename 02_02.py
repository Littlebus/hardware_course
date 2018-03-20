import RPi.GPIO as GPIO
import time
LED = 26
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)

def q1():
    try:
        while True:
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.2)
    except KeyboardInterrupt:
        GPIO.cleanup()
def q2():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED,GPIO.OUT)
    try:
        while True:
            p = GPIO.PWM(LED, 50)
            p.start(100)
            time.sleep(0.2)
            p.stop()
            time.sleep(0.2)
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()

def breathe():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED,GPIO.OUT)
    p = GPIO.PWM(LED,50)
    p.start(0)

    try:
        while True:
            for dc in range(0,101,5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.05)
            for dc in range(100,-1,-5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.05)
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    q1()
    q2()
    breathe()