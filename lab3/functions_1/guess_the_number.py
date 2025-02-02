#13
import random

def guess_the_number():
  lower_bound, upper_bound = 1, random.randint(1, 10)
  number_to_guess = random.randint(lower_bound, upper_bound)
  guesses_taken = 0

  name = input("Hello, What is your name?\n")
  print(f"Hello, {name}, I am thinling of a number between {lower_bound} and {upper_bound}.\nTake a guess.")

  while True:
    guess = int(input())

    if guess < number_to_guess:
      print("Your guess is too low.")
      guesses_taken += 1
      
      if guesses_taken == 3:
        print("Game over!")
        break
    elif guess > number_to_guess:
      print("Your guess is too high.")
      guesses_taken += 1
      if guesses_taken == 3:
        print("Game over!")
        break
    else:
      print("Good job! You've found the number")
      break

guess_the_number()