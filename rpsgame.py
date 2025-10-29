# a simple rock,paper,scissors game with the computer and user

import random

# Choices available
 
choices = ['rock','paper','scissors']

print("Welcome to Rock, Paper, Scissors!")
print("Type 'quit' anytime to exit\n")

while True:

    user = input("Enter your choice (rock/paper/scissors): ").lower()

    if user == 'quit':
        print("Thanks for playing, Goodbye!")
        break

    if user not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.\n")
        continue

    computer = random.choice(choices)

    print(f"Computer chose: {computer}")

    # Game logic

    if user == computer :
        print("Its a tie !")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        print("You Won !")
    else :
        print("You Lost !")

    print() #Just for Spacing


