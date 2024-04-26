import tkinter as tk
from tkinter import messagebox

# Karatsuba Algorithm
def karatsuba(x, y):
    steps = []
    if len(str(x)) == 1 or len(str(y)) == 1:
        result = x * y
        steps.append(f"Multiplying {x} and {y}: {result}")
        return result, steps
    else:
        n = max(len(str(x)), len(str(y)))
        nby2 = n // 2

        a = x // 10**(nby2)
        b = x % 10**(nby2)
        c = y // 10**(nby2)
        d = y % 10**(nby2)

        ac, steps_ac = karatsuba(a, c)
        bd, steps_bd = karatsuba(b, d)
        ad_bc, steps_ad_bc = karatsuba(a + b, c + d)
        ad_bc -= ac + bd

        result = ac * 10**(2*nby2) + (ad_bc * 10**nby2) + bd
        steps.append(f"Calculating a * c: {a} * {c} = {a * c}")
        steps.extend(steps_ac)
        steps.append(f"Calculating b * d: {b} * {d} = {b * d}")
        steps.extend(steps_bd)
        steps.append(f"Calculating (a + b) * (c + d): {(a + b)} * {(c + d)} = {(a + b) * (c + d)}")
        steps.extend(steps_ad_bc)
        steps.append(f"Result: {result}")

        return result, steps

# Strassen's Matrix Multiplication Algorithm
def strassen(matrix_a, matrix_b):
    steps = []
    if len(matrix_a) == 1:
        result = [[matrix_a[0][0] * matrix_b[0][0]]]
        steps.append(f"Multiplying matrices: {matrix_a} and {matrix_b}")
        return result, steps

    size = len(matrix_a)
    if size % 2 != 0:
        # Pad matrices if size is not a power of 2
        new_size = size + 1
        matrix_a = pad_matrix(matrix_a, new_size)
        matrix_b = pad_matrix(matrix_b, new_size)

    new_size = len(matrix_a) // 2

    # Divide matrices into submatrices
    a11, a12, a21, a22 = split_matrix(matrix_a)
    b11, b12, b21, b22 = split_matrix(matrix_b)

    # Compute 7 products recursively
    p1, steps_p1 = strassen(a11, subtract_matrices(b12, b22))
    p2, steps_p2 = strassen(add_matrices(a11, a12), b22)
    p3, steps_p3 = strassen(add_matrices(a21, a22), b11)
    p4, steps_p4 = strassen(a22, subtract_matrices(b21, b11))
    p5, steps_p5 = strassen(add_matrices(a11, a22), add_matrices(b11, b22))
    p6, steps_p6 = strassen(subtract_matrices(a12, a22), add_matrices(b21, b22))
    p7, steps_p7 = strassen(subtract_matrices(a11, a21), add_matrices(b11, b12))

    # Compute result submatrices
    c11 = add_matrices(subtract_matrices(add_matrices(p5, p4), p2), p6)
    c12 = add_matrices(p1, p2)
    c21 = add_matrices(p3, p4)
    c22 = subtract_matrices(subtract_matrices(add_matrices(p5, p1), p3), p7)

    # Combine submatrices into one result matrix
    result_matrix = combine_matrices(c11, c12, c21, c22)

    steps.append("Strassen's algorithm steps:")
    steps.extend(steps_p1)
    steps.extend(steps_p2)
    steps.extend(steps_p3)
    steps.extend(steps_p4)
    steps.extend(steps_p5)
    steps.extend(steps_p6)
    steps.extend(steps_p7)
    steps.append("Combining submatrices into one result matrix.")
    steps.append(f"Result: {result_matrix}")

    return result_matrix, steps

def split_matrix(matrix):
    size = len(matrix)
    mid = size // 2

    a11 = [row[:mid] for row in matrix[:mid]]
    a12 = [row[mid:] for row in matrix[:mid]]
    a21 = [row[:mid] for row in matrix[mid:]]
    a22 = [row[mid:] for row in matrix[mid:]]

    return a11, a12, a21, a22

def add_matrices(matrix_a, matrix_b):
    return [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a))] for i in range(len(matrix_a))]

def subtract_matrices(matrix_a, matrix_b):
    return [[matrix_a[i][j] - matrix_b[i][j] for j in range(len(matrix_a))] for i in range(len(matrix_a))]

def combine_matrices(a11, a12, a21, a22):
    size = len(a11)
    result_matrix = [[0] * (size * 2) for _ in range(size * 2)]

    for i in range(size):
        for j in range(size):
            result_matrix[i][j] = a11[i][j]
            result_matrix[i][j + size] = a12[i][j]
            result_matrix[i + size][j] = a21[i][j]
            result_matrix[i + size][j + size] = a22[i][j]

    return result_matrix

def pad_matrix(matrix, new_size):
    for row in matrix:
        row.extend([0] * (new_size - len(row)))
    matrix.extend([[0] * new_size] * (new_size - len(matrix)))
    return matrix

# GUI
def calculate_karatsuba():
    try:
        x = int(entry_x.get())
        y = int(entry_y.get())
        result, steps = karatsuba(x, y)
        messagebox.showinfo("Result", f"The result of Karatsuba multiplication is: {result}\n\nSteps:\n" + "\n".join(steps))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers for x and y.")

def calculate_strassen():
    try:
        matrix_a = eval(entry_matrix_a.get())
        matrix_b = eval(entry_matrix_b.get())

        if not isinstance(matrix_a, list) or not isinstance(matrix_b, list):
            raise ValueError("Please enter matrices as 2D lists.")

        if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
            messagebox.showerror("Error", "Matrices must have the same dimensions.")
            return

        result, steps = strassen(matrix_a, matrix_b)
        messagebox.showinfo("Result", f"The result of Strassen's matrix multiplication is: {result}\n\nSteps:\n" + "\n".join(steps))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main GUI window
root = tk.Tk()
root.title("Divide and Conquer Algorithms")

frame_karatsuba = tk.Frame(root)
frame_karatsuba.pack(pady=10)

label_x = tk.Label(frame_karatsuba, text="Enter x:")
label_x.grid(row=0, column=0, padx=5, pady=5)
entry_x = tk.Entry(frame_karatsuba)
entry_x.grid(row=0, column=1, padx=5, pady=5)
entry_x.insert(0, "Enter an integer")

label_y = tk.Label(frame_karatsuba, text="Enter y:")
label_y.grid(row=1, column=0, padx=5, pady=5)
entry_y = tk.Entry(frame_karatsuba)
entry_y.grid(row=1, column=1, padx=5, pady=5)
entry_y.insert(0, "Enter an integer")

button_karatsuba = tk.Button(frame_karatsuba, text="Calculate Karatsuba", command=calculate_karatsuba)
button_karatsuba.grid(row=2, columnspan=2, padx=5, pady=5)

frame_strassen = tk.Frame(root)
frame_strassen.pack(pady=10)

label_matrix_a = tk.Label(frame_strassen, text="Enter matrix A (2D list):")
label_matrix_a.grid(row=0, column=0, padx=5, pady=5)
entry_matrix_a = tk.Entry(frame_strassen)
entry_matrix_a.grid(row=0, column=1, padx=5, pady=5)
entry_matrix_a.insert(0, "[[1, 2], [3, 4]]")

label_matrix_b = tk.Label(frame_strassen, text="Enter matrix B (2D list):")
label_matrix_b.grid(row=1, column=0, padx=5, pady=5)
entry_matrix_b = tk.Entry(frame_strassen)
entry_matrix_b.grid(row=1, column=1, padx=5, pady=5)
entry_matrix_b.insert(0, "[[5, 6], [7, 8]]")

button_strassen = tk.Button(frame_strassen, text="Calculate Strassen", command=calculate_strassen)
button_strassen.grid(row=2, columnspan=2, padx=5, pady=5)

root.mainloop()
