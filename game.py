import random
import tkinter as tk
from tkinter import messagebox

choices = ("rock", "paper", "scissor")


def play_game(user_choice):
    ai_choice = random.choice(choices)
    result = ""
    if user_choice == ai_choice:
        result = "Tie"
    elif ((user_choice == 'rock' and ai_choice == 'scissor') or
          (user_choice == 'scissor' and ai_choice == 'paper') or
          (user_choice == 'paper' and ai_choice == 'rock')):
        result = "You win!"
    else:
        result = "AI wins!"
    result_label.config(text=f"AI chose: {ai_choice}\n{result}")


root = tk.Tk()
root.title("Rock Paper Scissors Game")

tk.Label(root, text="Choose Rock, Paper, or Scissor:",
         font=("Arial", 12), bg="#f0e68c").pack(pady=5)

button_frame = tk.Frame(root, bg="#f0e68c")
button_frame.pack(pady=5)

button_colors = {"rock": "#a2d5f2", "paper": "#b6e2d3", "scissor": "#f7cac9"}

for choice in choices:
    tk.Button(
        button_frame,
        text=choice.capitalize(),
        width=10,
        font=("Arial", 12, "bold"),
        bg=button_colors[choice],
        fg="#333",
        activebackground="#ffe066",
        command=lambda c=choice: play_game(c)
    ).pack(side=tk.LEFT, padx=8)

result_label = tk.Label(root, text="", font=(
    "Arial", 14, "bold"), pady=15, bg="#f0e68c")
result_label.pack()

footer_label = tk.Label(root, text="Have fun!", font=(
    "Comic Sans MS", 10, "italic"), fg="#4682b4", bg="#f0e68c")
footer_label.pack(pady=5)

root.mainloop()
