#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import random

# Basic GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set pin assignments
led = 4
rightButton = 14
leftButton = 15

# Generate a random time
randTime = random.uniform(5,10)

# Input player names
leftName = input("Player 1 enter your name: ")
rightName = input("Player 2 enter your name: ")
names = [leftName, rightName]

leftScore = 0
rightScore = 0
rounds = 0
maxRounds = 3

# Setup GPIO pins
GPIO.setup(led, GPIO.OUT)
GPIO.setup(rightButton, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(leftButton, GPIO.IN, GPIO.PUD_UP)

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
    time.sleep(randTime)

    # Turn off. First person to press wins!
    GPIO.output(led, 0)

    while True:
      # Loop waiting for first player to press
      if GPIO.input(leftButton) == False:
        print(names[0] + " won!")
        leftScore += 1
        break 
      if GPIO.input(rightButton) == False:
        print(names[1] + " won!")
        rightScore += 1
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

GPIO.cleanup()
