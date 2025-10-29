# Upraded version of Rock, Paper, Scissors Game with 5 rounds and track of scores

import random

choices = ['rock','paper','scissors']
emojis = {"rock":"🪨","paper":"📄","scissors":"✂️"}

user_score = 0
computer_score = 0
rounds = 0
max_rounds = 5

print("Welcome to Rock, Paper, Scissors Game !")
print("Type 'quit' anytime to exit \n")

while rounds < max_rounds:
    
    user = input("Enter your choice (rock/paper/scissors): ").lower()
    if user == 'quit':
        print("\nGame Ended Early !👋")
        break

    if user not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors. \n")
        continue

    computer = random.choice(choices)

    print(f"User: {emojis[user]}  vs  Computer: {emojis[computer]}")
    
    #Determine winner of the round

    if user == computer:
        print("It's a tie this round! 🤝")
    elif (user == 'rock' and computer == 'scissors') or \
            (user == 'paper' and computer == 'rock') or \
            (user == 'scissors' and computer == 'paper'):
        print("You won this round! 🎉")
        user_score +=1
    else:
        print("Computer won this round! 🤖")
        computer_score +=1
    
    rounds +=1
    print(f"Score -> You: {user_score} - {computer_score} Computer")

#Final Results

print("🏁 Game Ended")
if user_score>computer_score:
    print("You Won the Game Congrats !")
if user_score<computer_score:
    print("You Lost the Game Better Luck Next Time")
else:
    print("Its a tie overall !")

print(f"Final Scores : You {user_score} - {computer_score} Computer")