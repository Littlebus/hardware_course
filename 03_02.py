from temp import *
import RPi.GPIO as GPIO

LED = 26
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
p = GPIO.PWM(LED, 1)
p.start(0)

def main():
    while True:
        print(' C=%3.3f F=%3.3f' % read_temp())
        if read_temp()[0] < 33.0:
            p.ChangeDutyCycle(0)
        else:
            p.ChangeDutyCycle(50)

if __name__ == '__main__':
    main()