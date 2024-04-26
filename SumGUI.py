import tkinter as tk

def calculate_sum():
    try:
        number = int(entry.get())
        result = sum(range(1, number + 1))
        result_label.config(text=f"Result: {'+'.join(map(str, range(1, number + 1)))} = {result}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Create the main window
window = tk.Tk()
window.title("Number Addition")
window.geometry("400x200")  # Set window size

# Create label and entry widget
tk.Label(window, text="Enter a number:", font=("Arial", 14)).pack()
entry = tk.Entry(window, font=("Arial", 14))
entry.pack()

# Create calculate button
calculate_button = tk.Button(window, text="Calculate", font=("Arial", 14), command=calculate_sum)
calculate_button.pack()

# Create label to display result
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack()

# Run the GUI
window.mainloop()
