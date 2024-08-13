import tkinter as tk
from tkinter import messagebox

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values.")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values.")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values.")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            raise ValueError("Division by zero")
        result = num1 / num2
        result_label.config(text=f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry fields
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=1, padx=10, pady=10)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create labels
label1 = tk.Label(root, text="First Number:")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Second Number:")
label2.grid(row=1, column=0)

# Create buttons
add_button = tk.Button(root, text="+", command=add)
add_button.grid(row=2, column=0)

subtract_button = tk.Button(root, text="-", command=subtract)
subtract_button.grid(row=2, column=1)

multiply_button = tk.Button(root, text="*", command=multiply)
multiply_button.grid(row=2, column=2)

divide_button = tk.Button(root, text="/", command=divide)
divide_button.grid(row=2, column=3)

# Create result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=3, column=0, columnspan=4, pady=10)

# Run the main loop
root.mainloop()