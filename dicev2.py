import tkinter as tk
import random

#dice faces as emojis
dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

#function to roll dice

def roll_dice():
    dice = random.choice(dice_faces)
    dice_label.config(text=dice, font=("Arial", 80))
    result_label.config(text=f"You rolled {dice_faces.index(dice)+1}")


# Setup window
window = tk.Tk()
window.title("🎲 Dice Roller")
window.config(padx=30, pady=30, bg="#1e1e2f")

title = tk.Label(window, text="🎲 Dice Roller", font=("Arial", 24, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=10)

dice_label = tk.Label(window, text="?", font=("Arial", 80), fg="#1e1e2f")
dice_label.pack(pady=20)

roll_button = tk.Button(window, text="Roll Dice", font=("Arial", 16, "bold"), bg="#4e4ea3", fg="white", width=15, command=roll_dice)
roll_button.pack(pady=10)

result_label = tk.Label(window, text="Click Roll to start!", font=("Arial", 14), bg="#1e1e2f", fg="skyblue")
result_label.pack(pady=10)

quit_button = tk.Button(window, text="Quit", font=("Arial", 12,"bold"), bg="crimson", fg="white", command=window.destroy)
quit_button.pack(pady=10)

window.mainloop()