#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import random

# Basic GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set pin assignments
led = 4
buzzer = 18
rightButton = 14
leftButton = 15
leftScoreLeds = [10,9,11]
rightScoreLeds = [18,22,23]

# Set up game variables
leftScore = 0
rightScore = 0
rounds = 0
maxRounds = 3

# Input player names
leftName = input("Player 1 enter your name: ")
rightName = input("Player 2 enter your name: ")
names = [leftName, rightName]

# Setup GPIO pins
GPIO.setup(led, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(rightButton, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(leftButton, GPIO.IN, GPIO.PUD_UP)

# Setup Score LEDs
for i in leftScoreLeds:
  GPIO.setup(i, GPIO.OUT)
  GPIO.output(i, 0)
for i in rightScoreLeds:
  GPIO.setup(i, GPIO.OUT)
  GPIO.output(i, 0)

while True:

  while rounds < maxRounds:
    rounds += 1
    print("Ready?...")
    print("Next round in")
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Go!...")

    # Turn LED on then wait for a random time
    GPIO.output(led, 1)
    GPIO.output(buzzer, 0)

    # Generate a random time
    randTime = random.uniform(5,10)

    # Sleep for random amount of time
    time.sleep(randTime)

    # Turn off. First person to press wins!
    GPIO.output(led, 0)
    GPIO.output(buzzer,1)

    while True:
      # Loop waiting for first player to press
      if GPIO.input(leftButton) == False:
        print(names[0] + " won!")
        leftScore += 1
        GPIO.output(buzzer,0)
        GPIO.output(leftScoreLeds[leftScore-1], 1)
        break 
      if GPIO.input(rightButton) == False:
        print(names[1] + " won!")
        rightScore += 1
        GPIO.output(buzzer,0)
        GPIO.output(rightScoreLeds[rightScore-1], 1)
        break

    # Ready for next game...?
    print("Score after " + str(rounds))
    print(names[0] + ": " + str(leftScore))
    print(names[1] + ": " + str(rightScore))

  break

if leftScore > rightScore:
  winner = names[0]
else:
  winner = names[1]

print("Winner:" + winner)

time.sleep(10)

GPIO.cleanup()
