import RPi.GPIO as GPIO
import time

KEY = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY, GPIO.IN, GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(KEY, GPIO.RISING, bouncetime=200)  
    print('KEY PRESS')
