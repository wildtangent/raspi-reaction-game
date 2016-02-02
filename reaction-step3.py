import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 4
leftButton = 14
rightButton = 15

GPIO.setup(led, GPIO.OUT)
GPIO.setup(leftButton, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(rightButton, GPIO.IN, GPIO.PUD_UP)

GPIO.output(led, 1)
randomTime = random.uniform(5,10)
time.sleep(randomTime)
GPIO.output(led, 0)

while True
  if GPIO.input(leftButton) == False  
    print("Left button won!")
    break
  if GPIO.input(rightButton) == False
    print("Right button won!")
    break

GPIO.cleanup()
