import tkinter as tk
from tkinter import Canvas

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

def fibonacci_nonrecursive(n):
    fib_sequence = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_sequence
    else:
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

def calculate_fibonacci():
    try:
        number = int(entry.get())
        if number > 0:
            fib_sequence_recursive = fibonacci_recursive(number)
            formatted_recursive_sequence = ', '.join(map(str, fib_sequence_recursive))
            result_text_recursive.delete(1.0, tk.END)
            result_text_recursive.insert(tk.END, f"Recursive Fibonacci Sequence: {formatted_recursive_sequence}")

            fib_sequence_nonrecursive = fibonacci_nonrecursive(number)
            formatted_nonrecursive_sequence = ', '.join(map(str, fib_sequence_nonrecursive))
            result_text_nonrecursive.delete(1.0, tk.END)
            result_text_nonrecursive.insert(tk.END, f"Non-recursive Fibonacci Sequence: {formatted_nonrecursive_sequence}")

            exit_label.place(x=20, y=max(result_text_recursive.winfo_height(), result_text_nonrecursive.winfo_height()) + 200)
            exit_label.config(text="Program done. Now Exiting...")
        else:
            result_text_recursive.delete(1.0, tk.END)
            result_text_recursive.insert(tk.END, "Please enter a positive integer.")
            result_text_nonrecursive.delete(1.0, tk.END)
            result_text_nonrecursive.insert(tk.END, "")
            exit_label.config(text="")
    except ValueError:
        result_text_recursive.delete(1.0, tk.END)
        result_text_recursive.insert(tk.END, "Please enter a valid number.")
        result_text_nonrecursive.delete(1.0, tk.END)
        result_text_nonrecursive.insert(tk.END, "")
        exit_label.config(text="")

# Creating the main window for the Graphical User Interface(GUI)
window = tk.Tk()
window.title("Fibonacci Sequence")


window.resizable(0, 0)

# Creating a Canvas Background Color
canvas = Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight(), bg='#e6e6e6')
canvas.pack(fill="both", expand=True)

# GREEN Grid with black lines
for i in range(0, window.winfo_screenwidth(), 20):
    for j in range(0, window.winfo_screenheight(), 20):
        canvas.create_rectangle(i, j, i + 20, j + 20, fill='#8fd9a8')

# Creating a label and widget window where the user will Input a number
tk.Label(window, text="Enter a number:", font=("Arial", 14), bg='#e6e6e6').place(x=20, y=20)
entry = tk.Entry(window, font=("Arial", 14))
entry.place(x=170, y=20)

# Creating the calculate button
calculate_button = tk.Button(window, text="Calculate", font=("Arial", 14), command=calculate_fibonacci)
calculate_button.place(x=400, y=20)

# Create text widget to display recursive result
result_text_recursive = tk.Text(window, font=("Arial", 12), width=60, height=5)
result_text_recursive.place(x=20, y=60)

# Create text widget to display non-recursive result
result_text_nonrecursive = tk.Text(window, font=("Arial", 12), width=60, height=5)
result_text_nonrecursive.place(x=20, y=150)

# Label for recursive function code
recursive_label = tk.Label(window, text="def fibonacci_recursive(n):\nif n <= 0:\nreturn []\n    elif n == 1:\nreturn [0]\nelif n == 2:\nreturn [0, 1]\n else:\nfib_sequence = fibonacci_recursive(n - 1)\n        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])\n        return fib_sequence", font=("Arial", 12), bg='#e6e6e6', justify=tk.LEFT)
recursive_label.place(x=650, y=60)

# Label for non-recursive function code
nonrecursive_label = tk.Label(window, text="def fibonacci_nonrecursive(n):\nfib_sequence = [0, 1]\nif n <= 0:\n return []\n elif n == 1:\nreturn [0]\nelif n == 2:\n return fib_sequence\n else:\n  for i in range(2, n):\n            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])\n        return fib_sequence", font=("Arial", 12), bg='#e6e6e6', justify=tk.LEFT)
nonrecursive_label.place(x=650, y=150)

# Create exit label
exit_label = tk.Label(window, text="", font=("Arial", 12), bg='#e6e6e6')
exit_label.place(x=20, y=max(result_text_recursive.winfo_height(), result_text_nonrecursive.winfo_height()) + 100)  # Adjust initial position of exit label

# Run the FIBONACCI MACHINE with GUI
window.mainloop()
