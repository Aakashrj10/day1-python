# A simple number guessing game

import random

number= random.randint(1,100)
guess=0

while guess!= number:
    guess=int(input("Enter your guess between 1 and 100: "))
    if guess < number:
        print("Too Low ! Try again.")
    elif guess > number :
        print("Too High ! Try again.")
    elif guess == number:
        print("You got it right! The number was", number)