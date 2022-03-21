# import random module
import random

# create a function
def guess(a):
  # generate random integer between 1 and the number that the user inputs. Store into a variable named "generate"
  generate = random.randint(1,a)
  # set guess = 0 to kickstart the first line after the while loop (guess = 0 satisfies guess != generate because 0 is not between 1 and a)
  guess = 0
  while guess != generate:
    guess = int(input(f'The computer has generated a number between 1 and {a}. Please guess this number.'))
    if guess < generate:
      print("Your guess is wrong. It is too low. Please guess a higher number.")
    elif guess > generate:
      print("Your guess is wrong. It is too high. Please guess a lower number.")
  # if guess = generate, the while loop will be broken (if elif statements will not execute) and the following will print
  print("You are right!")

# call the function
guess(10)
