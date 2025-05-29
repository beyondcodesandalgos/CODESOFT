import tkinter as tk
import random

# Password components
letters_l = list("abcdefghijklmnopqrstuvwxyz")
letters_u = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("123456789")
special_signs = ['-', '_', '.', ',', ':', ';', '#', '$', '&', '*', '@']

# Function to generate password
def generate_password():
    length_input = length_entry.get().strip()  # Read input and remove whitespace
    if not length_input.isdigit() or int(length_input) <= 0:
        password_label.config(text="Please enter a valid number!", fg="red")
        return
    
    length = int(length_input)  # Convert to integer
    password_components = letters_l + letters_u + numbers + special_signs
    password = ''.join(random.choices(password_components, k=length))
    password_label.config(text=password, fg="#00FF00")  # Display password

# Main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.config(bg="black")

# Title label
title_label = tk.Label(root, text="Generate a Secure Password!", font=("Arial", 16, "bold"), fg="#FF9500", bg="black")
title_label.pack(padx=20, pady=10)

# Entry to specify password length
length_label = tk.Label(root, text="Enter Password Length:", font=("Arial", 12), fg="white", bg="black")
length_label.pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12), bg="#333333", fg="white", insertbackground="white")
length_entry.pack(pady=5)

# Button to generate password with styling
generate_button = tk.Button(root, text="Generate", font=("Arial", 12, "bold"), bg="#FF9500", fg="white", padx=10, pady=5, relief="flat", command=generate_password)
generate_button.pack(pady=10)

# Label to display password with modern styling
password_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="black", fg="white")
password_label.pack(pady=10)

root.mainloop()