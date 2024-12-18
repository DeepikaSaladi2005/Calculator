import tkinter as tk
from tkinter import messagebox

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def modulus(a, b):
    return a % b

def append_to_entry(value):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, current + str(value))

def clear_entry():
    entry_display.delete(0, tk.END)

def append_operator(op):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, current + f" {op} ")

def calculate():
    try:
        parts = entry_display.get().split()
        if len(parts) != 3:
            raise ValueError("Please enter a valid expression in the format: number1 operator number2.")

        num1, operator, num2 = float(parts[0]), parts[1], float(parts[2])

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        elif operator == "%":
            result = modulus(num1, num2)
        else:
            raise ValueError("Unknown operator.")

        label_result.config(text=f"Result: {result}", fg="blue")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#f0f8ff")

# Display entry
entry_display = tk.Entry(root, font=("Arial", 14), width=30, justify='right')
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Number buttons
def create_number_button(value, row, col):
    return tk.Button(root, text=str(value), font=("Arial", 14), bg="#d3d3d3", command=lambda: append_to_entry(value)).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=5)

numbers = [
    (1, 1, 0), (2, 1, 1), (3, 1, 2),
    (4, 2, 0), (5, 2, 1), (6, 2, 2),
    (7, 3, 0), (8, 3, 1), (9, 3, 2),
    (0, 4, 1)
]

for num, row, col in numbers:
    create_number_button(num, row, col)

# Clear button
button_clear = tk.Button(root, text="C", font=("Arial", 14), bg="#ffcccb", command=clear_entry)
button_clear.grid(row=4, column=0, padx=5, pady=5, ipadx=10, ipady=5)

# Operation buttons
button_add = tk.Button(root, text="+", font=("Arial", 14), bg="#add8e6", command=lambda: append_operator("+"))
button_add.grid(row=1, column=3, padx=5, pady=5, ipadx=10, ipady=5)

button_subtract = tk.Button(root, text="-", font=("Arial", 14), bg="#ffa07a", command=lambda: append_operator("-"))
button_subtract.grid(row=2, column=3, padx=5, pady=5, ipadx=10, ipady=5)

button_multiply = tk.Button(root, text="*", font=("Arial", 14), bg="#98fb98", command=lambda: append_operator("*"))
button_multiply.grid(row=3, column=3, padx=5, pady=5, ipadx=10, ipady=5)

button_divide = tk.Button(root, text="/", font=("Arial", 14), bg="#f08080", command=lambda: append_operator("/"))
button_divide.grid(row=4, column=3, padx=5, pady=5, ipadx=10, ipady=5)

button_modulus = tk.Button(root, text="%", font=("Arial", 14), bg="#dda0dd", command=lambda: append_operator("%"))
button_modulus.grid(row=4, column=2, padx=5, pady=5, ipadx=10, ipady=5)

# Equals button
button_equals = tk.Button(root, text="=", font=("Arial", 14), bg="#90ee90", command=calculate)
button_equals.grid(row=5, column=3, padx=5, pady=5, ipadx=10, ipady=5)

# Result label
label_result = tk.Label(root, text="Result: ", font=("Arial", 14), bg="#f0f8ff")
label_result.grid(row=5, column=0, columnspan=4, pady=20)

# Run the application
root.mainloop()
