import tkinter as tk
import random

# Game choices
choices = ["Rock", "Paper", "Scissors"]

# Scores
cpu_score = 0
player_score = 0

# Function to play the game
def play(player_choice):
    global cpu_score, player_score
    computer_choice = random.choice(choices)
    
    # Display computer's choice in a separate label
    comp_choice_label.config(text=f"Computer chose: {computer_choice}", fg="blue")

    # Determine the result
    if player_choice == computer_choice:
        result_text = "It's a tie!"
        result_label.config(text=result_text, fg="gray")  # Neutral color
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result_text = f"You win! {player_choice} beats {computer_choice}"
        result_label.config(text=result_text, fg="green")  # Winning color
        player_score += 1
    else:
        result_text = f"You lose! {computer_choice} beats {player_choice}"
        result_label.config(text=result_text, fg="red")  # Losing color
        cpu_score += 1
    
    # Update scores
    score_label.config(text=f"Player: {player_score} | Computer: {cpu_score}")

# Function to reset the game
def reset_game():
    global cpu_score, player_score
    cpu_score = 0
    player_score = 0
    comp_choice_label.config(text="Computer's choice will appear here", fg="black")
    result_label.config(text="Make your choice!", fg="black")
    score_label.config(text="Player: 0 | Computer: 0")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x300")
root.config(bg="#ffe799")

# Title label
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"), bg="#ffe799")
title_label.pack(pady=10)

# Buttons frame
frame = tk.Frame(root, bg="#ffe799")
frame.pack(pady=10)

for choice in choices:
    tk.Button(frame, text=choice, width=12, font=("Arial", 12), bg="#add8e6", 
              command=lambda c=choice: play(c)).pack(side="left", padx=5)

# Computer's choice label (Separate for clarity)
comp_choice_label = tk.Label(root, text="Computer's choice will appear here", font=("Arial", 12), bg="#ffe799", fg="black")
comp_choice_label.pack(pady=5)

# Result label
result_label = tk.Label(root, text="Make your choice!", font=("Arial", 12), bg="#ffe799", pady=10, fg="black")
result_label.pack()

# Score label
score_label = tk.Label(root, text="Player: 0 | Computer: 0", font=("Arial", 12, "bold"), bg="#ffe799", fg="darkgreen")
score_label.pack(pady=5)

# Reset button
reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12), bg="#ffcccb", command=reset_game)
reset_button.pack(pady=10)

# Run the Tkinter loop
root.mainloop()