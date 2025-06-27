import tkinter as tk
import random

def play(user_action):
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    
    result_text = f"You chose {user_action}, computer chose {computer_action}.\n"
    
    if user_action == computer_action:
        result_text += f"Both players selected {user_action}. It's a tie!"
    elif user_action == "rock":
        if computer_action == "scissors":
            result_text += "Rock smashes scissors! You win!"
        else:
            result_text += "Paper covers rock! You lose."
    elif user_action == "paper":
        if computer_action == "rock":
            result_text += "Paper covers rock! You win!"
        else:
            result_text += "Scissors cuts paper! You lose."
    elif user_action == "scissors":
        if computer_action == "paper":
            result_text += "Scissors cuts paper! You win!"
        else:
            result_text += "Rock smashes scissors! You lose."
    
    result_label.config(text=result_text)

root = tk.Tk()
root.title("Rock Paper Scissors")

instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
instruction_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue", wraplength=300, justify="center")
result_label.pack(pady=20)

root.mainloop()
