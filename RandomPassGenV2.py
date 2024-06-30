import random
import string
import tkinter as tk
from tkinter import ttk

def generate_random_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars, use_ultra ):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits 
    if use_ultra:
        characters += string.ultra
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "Select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_digits = digits_var.get()
    use_ultra = ultra_var.get()
    use_special_chars = special_chars_var.get()

    password = generate_random_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
    password_display.delete(1.0, tk.END)  # Clear previous content
    password_display.insert(tk.END, password)

# Create GUI window
root = tk.Tk()
root.title("RDM by ServerDowner")

# Length label and entry
length_label = ttk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, sticky="w")
length_entry = ttk.Entry(root)
length_entry.insert(0, "12")
length_entry.grid(row=0, column=1)

# Character options
uppercase_var = tk.BooleanVar()
uppercase_check = ttk.Checkbutton(root, text="Uppercase", variable=uppercase_var)
uppercase_check.grid(row=1, column=0, sticky="w")

lowercase_var = tk.BooleanVar()
lowercase_check = ttk.Checkbutton(root, text="Lowercase", variable=lowercase_var)
lowercase_check.grid(row=2, column=0, sticky="w")

digits_var = tk.BooleanVar()
digits_check = ttk.Checkbutton(root, text="Digits", variable=digits_var)
digits_check.grid(row=3, column=0, sticky="w")

special_chars_var = tk.BooleanVar()
special_chars_check = ttk.Checkbutton(root, text="Special Characters", variable=special_chars_var)
special_chars_check.grid(row=4, column=0, sticky="w")

ultra_var = tk.BooleanVar()
ultra_check = ttk.Checkbutton(root, text="Ultra Characters", variable=ultra_var)
ultra_check.grid(row=5, column=0, sticky="w")

# Generate button
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=6, column=0, columnspan=2)

# Generated password display box (smaller size)
password_display = tk.Text(root, height=2, width=30)  # Adjusted height
password_display.grid(row=7, column=0, columnspan=2)

# Start GUI event loop
root.mainloop()
