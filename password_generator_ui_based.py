import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be positive")
        password = generate_password(length)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
label_length = tk.Label(root, text="Enter Password Length:")
label_length.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=on_generate)
button_generate.pack(pady=5)

label_password = tk.Label(root, text="Generated Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(root)
entry_password.pack(pady=5)

# Run the application
root.mainloop()
