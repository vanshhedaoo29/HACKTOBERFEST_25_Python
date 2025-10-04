import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    """
    Generate a random password containing at least
    one letter, one digit, and one symbol.
    Display it in the read-only password entry.
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

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one letter, digit, symbol
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - 3)
    random.shuffle(password)
    password_str = ''.join(password)

    # Display password in read-only entry
    password_entry.config(state='normal')
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password_str)
    password_entry.config(state='readonly')

def copy_to_clipboard():
    #Copy the generated password to the clipboard.
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x220")
root.resizable(False, False)


tk.Label(root, text="Enter password length:").pack(pady=10)
length_entry = tk.Entry(root)
length_entry.pack()


tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

#Read-only password entry
password_entry = tk.Entry(root, width=40, state='readonly')
password_entry.pack(pady=10)


tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)

root.mainloop()
