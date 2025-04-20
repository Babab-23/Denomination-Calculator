import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
        strength = "Please enter a password."
    elif length < 6:
        strength = "Weak"
    elif 6 <= length <= 10:
        strength = "Medium"
    else:
        strength = "Strong"

    result_label.config(text=f"Password Strength: {strength}")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")

# Create and place widgets
label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(root, show='*', width=30)
entry.pack()

check_button = tk.Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI event loop
root.mainloop()
