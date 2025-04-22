# 0-hello_gui_tkinter.py

# Importing tkinter module and messagebox for pop-up dialogs
import tkinter as tk
from tkinter import messagebox

# Function to greet the user when the button is clicked
def greet():
    name = name_entry.get()  # Get text from the input field
    if name.strip():  # Check if name is not empty or just whitespace
        messagebox.showinfo("Greeting", f"Hello, {name}!")  # Show a pop-up greeting
    else:
        messagebox.showwarning("Input needed", "Please enter your name.")  # Show warning if input is empty

# Create the main application window
root = tk.Tk()  # Initialize the main window
root.title("Greeter App")  # Set the title of the window
root.geometry("300x150")  # Set the dimensions of the window (width x height)

# Create and place a label widget
tk.Label(root, text="Enter your name:").pack(pady=10)  # Display a prompt with vertical padding

# Create and place an entry widget for name input
name_entry = tk.Entry(root)  # Create an input field
name_entry.pack(pady=5)  # Add it to the window with vertical padding

# Create and place a button widget
tk.Button(root, text="Greet Me", command=greet).pack(pady=10)  # Button triggers the greet() function

# Start the main GUI event loop
root.mainloop()  # Keeps the window open and responsive
