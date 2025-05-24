import tkinter as tk
import random

# Lists for password components
letters_l = list("abcdefghijklmnopqrstuvwxyz")
letters_u = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("123456789")
special_signs = ['-', '_', '.', '#', '$', '&', '*', '@']
animals = ["horses", "unicorns", "tiger", "dogs", "cats"]

# Function to generate password
def generate_password():
    letter_1 = random.choice(letters_l)
    num = random.choice(numbers)
    sign = random.choice(special_signs)
    ani = random.choice(animals).capitalize()
    letter_2 = random.choice(letters_u)
    
    password = letter_1 + num + sign + ani + letter_2
    password_label.config(text=password)

# Setting up the GUI
root = tk.Tk()
root.title("Student-Friendly Password Generator")
root.geometry("300x200")
root.config(bg="#ffe799")

# Title label
title_label = tk.Label(root, text="Generate a Secure Password!", font=("Arial", 12),bg="#ffe799")
title_label.pack(pady=10)

# Button to generate password
generate_button = tk.Button(root, text="Generate", command=generate_password, font=("Arial", 10))
generate_button.pack(pady=5)

# Label to display password
password_label = tk.Label(root, text="", font=("Arial", 12), bg="#ffe799", fg="blue")
password_label.pack(pady=10)

# Run the Tkinter loop
root.mainloop()