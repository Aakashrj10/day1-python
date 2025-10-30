# a simple dice rolling simulator
import random 

print("Welcome to the Dice Rolling Simulator!")
print("Type 'roll' to roll the dice or 'quit' to exit.")

while True:
    user = input(">>> ").lower()
    if user == "quit":
        print("Thanks for playing! Goodbye!")
        break
    elif user == "roll":
        dice = random.randint(1, 6)
        print(f"You rolled a {dice}!")
    else:
        print("Invalid command. Please type 'roll' or 'quit'.")
        
