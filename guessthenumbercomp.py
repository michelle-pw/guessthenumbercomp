import random

def guess(a):
  generate = random.randint(1,a)
  guess = 0
  while guess != generate:
    guess = int(input(f'The computer has generated a number between 1 and {a}. Please guess this number.'))
    if guess < generate:
      print("Your guess is wrong. It is too low. Please guess a higher number.")
    elif guess > generate:
      print("Your guess is wrong. It is too high. Please guess a lower number.")
  print("You are right!")

guess(10)
