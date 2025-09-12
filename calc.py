import tkinter as tk
from tkinter import messagebox

def calculate():
    """
    This function retrieves input values from the entry fields,
    performs the specified arithmetic operation, and displays
    the result on the label. It handles invalid inputs and division
    by zero with appropriate error messages.
    """
    try:
        # Get first number from input field and convert to float
        num1 = float(entry_num1.get())
        # Get second number from input field and convert to float
        num2 = float(entry_num2.get())
        # Get the operation selected by the user
        op = var_op.get()

        # Perform calculation based on the selected operator
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            # Handle division by zero error
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            # Show error message if invalid operation is selected
            messagebox.showerror("Error", "Invalid operation!")
            return

        # Show the calculation result on the label
        label_result.config(text=f"Result: {result}")

    except ValueError:
        # Show error message if the inputs are not valid numbers
        messagebox.showerror("Error", "Enter valid numbers!")
    except ZeroDivisionError:
        # Show error message for division by zero
        messagebox.showerror("Error", "Cannot divide by zero!")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Label and entry for the first number input
tk.Label(root, text="Enter first number:").grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

# Label and entry for the second number input
tk.Label(root, text="Enter second number:").grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

# Label and dropdown menu for selecting the operation
tk.Label(root, text="Operation:").grid(row=2, column=0)
var_op = tk.StringVar(value="+")  # Default value is '+'
tk.OptionMenu(root, var_op, "+", "-", "*", "/").grid(row=2, column=1)

# Button that triggers the calculation when clicked
tk.Button(root, text="Calculate", command=calculate).grid(row=3, columnspan=2)

# Label to display the calculation result
label_result = tk.Label(root, text="Result:")
label_result.grid(row=4, columnspan=2)

# Run the Tkinter event loop (keeps window open)
root.mainloop()
# Hey