import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

rounds = 0
led = 4
leftButton = 14
rightButton = 15
leftScore = 0
rightScore = 0
leftName = input("Player 1 enter your name: ")
rightName = input("Player 2 enter your name: ")

GPIO.setup(led, GPIO.OUT)
GPIO.setup(leftButton, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(rightButton, GPIO.IN, GPIO.PUD_UP)


while True:
  while rounds < 3:
    rounds += 1
    
    GPIO.output(led, 1)
    randomTime = random.uniform(5,10)
    time.sleep(randomTime)
    GPIO.output(led, 0)

    while True:
      if GPIO.input(leftButton) == False: 
        print(leftName + " was the winner!")
        leftScore += 1
        break
      if GPIO.input(rightButton) == False:
        print(rightName + " was the winner!")
        rightScore += 1
        break

    print("Score after " + str(rounds) + " rounds")
    print("Player 1: " + str(leftScore))
    print("Player 2: " + str(rightScore))
    
  break

if leftScore > rightScore:
  winner = leftName
  score = leftScore
else:
  winner = rightName
  score = rightScore

print(winner + " was the winner with " + str(score) + " points1")

GPIO.cleanup()
