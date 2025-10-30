# Improved version with tinker for gui

import tkinter as tk
import random

window = tk.Tk()
window.title("Rock, Paper, Scissors 🎮")
window.config(padx = 30, pady =30, bg="#1e1e2f")

choices = ["rock", "paper", "scissors"]
emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

user_score=0
comp_score=0


def play(user_choice):
    global user_score , comp_score
    computer_choice =random.choice(choices)

    user_label.config(text=f"You: {emojis[user_choice]}")
    comp_label.config(text=f"Computer : {emojis[computer_choice]}")

    if user_choice == computer_choice:
        result_label.config(text="It's a Tie 😐", fg="orange")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result_label.config(text="You Win! 🎉", fg="lightgreen")
        user_score += 1
    else:
        result_label.config(text="You Lose 💀", fg="red")
        comp_score += 1

    score_label.config(text=f"Score: You {user_score} - {comp_score} Computer")

# ----- UI Elements -----

title = tk.Label(window, text="Rock, Paper, Scissors", font=("Arial", 24, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=10)

user_label = tk.Label(window, text="You: ", font=("Arial", 18), bg="#1e1e2f", fg="white")
user_label.pack()

comp_label = tk.Label(window, text="Computer: ", font=("Arial", 18), bg="#1e1e2f", fg="white")
comp_label.pack(pady=5)

result_label = tk.Label(window, text="Make your choice!", font=("Arial", 18), bg="#1e1e2f", fg="white")
result_label.pack(pady=15)

score_label = tk.Label(window, text="Score: You 0 - 0 Computer", font=("Arial", 16), bg="#1e1e2f", fg="white")
score_label.pack(pady=10)

#Buttons
button_frame = tk.Frame(window, bg="#1e1e2f")
button_frame.pack(pady=10)

for choice in choices:
    tk.Button(
        button_frame,
        text=f"{emojis[choice]} {choice.capitalize()}",
        font=("Arial", 20),
        width=12,
        bg="#3c3c55",
        fg="white",
        relief="raised",
        command=lambda c=choice: play(c)
    ).pack(side="left", padx=8)

# Exit button
exit_button = tk.Button(window, text="Exit", font=("Arial", 14), bg="#ff4c4c", fg="white", command=window.quit)
exit_button.pack(pady=10)

# --- Run ---
window.mainloop()