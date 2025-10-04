import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    """
    Generate a random password based on user-selected options:
    - Length
    - Inclusion of letters, digits, symbols
    """
    try:
        length = int(length_entry.get())
        if length < 3:
            messagebox.showerror("Error", "Password length must be at least 3")
            return
        if length > 50:
            messagebox.showerror("Error", "Password length must not exceed 50")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
        return

    # Gather character sets based on checkboxes
    all_chars = ""
    required_chars = []

    if include_letters.get():
        all_chars += string.ascii_letters
        required_chars.append(random.choice(string.ascii_letters))

    if include_digits.get():
        all_chars += string.digits
        required_chars.append(random.choice(string.digits))

    if include_symbols.get():
        all_chars += string.punctuation
        required_chars.append(random.choice(string.punctuation))

    if not all_chars:
        messagebox.showerror("Error", "Select at least one character type")
        return

    # Fill the rest of the password
    remaining_length = length - len(required_chars)
    password = required_chars + random.choices(all_chars, k=remaining_length)

    random.shuffle(password)
    password_str = ''.join(password)

    # Display password in read-only entry
    password_entry.config(state='normal')
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password_str)
    password_entry.config(state='readonly')

def copy_to_clipboard():
    """
    Copy the generated password to the clipboard
    """
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

def is_digit_input(input_str):
    """
    Validate that only digits are allowed in the entry
    """
    return input_str.isdigit() or input_str == ""

# ---- GUI Setup ----
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Instruction Label
tk.Label(root, text="Enter password length:").pack(pady=(10, 2))

# Entry for length (with digit-only validation)
vcmd = (root.register(is_digit_input), '%P')
length_entry = tk.Entry(root, validate='key', validatecommand=vcmd)
length_entry.insert(0, "12")  # Default value
length_entry.pack(pady=2)

# Checkboxes for character types
include_letters = tk.BooleanVar(value=True)
include_digits = tk.BooleanVar(value=True)
include_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=include_letters).pack()
tk.Checkbutton(root, text="Include Digits", variable=include_digits).pack()
tk.Checkbutton(root, text="Include Symbols", variable=include_symbols).pack()

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Read-only password output
password_entry = tk.Entry(root, width=40, state='readonly', justify='center')
password_entry.pack(pady=10)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()

# Run the GUI
root.mainloop()
