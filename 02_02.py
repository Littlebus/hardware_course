import PRi.GPIO as GPIO
import time
LED = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
def q1():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(LED, GPIO.LOW)

def q2():
    p = GPIO.PWM(LED, 50)
    p.start(100)
    time.sleep(0.2)
    p.stop()

def breathe():
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
