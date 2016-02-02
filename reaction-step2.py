import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 4

GPIO.setup(led, GPIO.OUT)

GPIO.output(led, 1)
randomTime = random.uniform(5,10)
time.sleep(randomTime)
GPIO.output(led, 0)

GPIO.cleanup()
