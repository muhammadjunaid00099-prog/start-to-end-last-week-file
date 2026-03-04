import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        feet = float(feet_entry.get())
        inches = float(inches_entry.get())

        height = (feet * 12 + inches) * 0.0254
        bmi = weight / (height ** 2)

        result_label.config(text=f"Your BMI is: {bmi:.2f}")

        if bmi <= 18.5:
            status_label.config(text="You are Underweight")
        elif 18.5 < bmi <= 25:
            status_label.config(text="You are Normal weight")
        elif 25 < bmi <= 30:
            status_label.config(text="You are Overweight")
        else:
            status_label.config(text="You are Obese")

    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Main Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Labels & Entry Fields
tk.Label(root, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (Feet):").pack(pady=5)
feet_entry = tk.Entry(root)
feet_entry.pack()

tk.Label(root, text="Height (Inches):").pack(pady=5)
inches_entry = tk.Entry(root)
inches_entry.pack()

# Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=15)

# Result Labels
result_label = tk.Label(root, text="")
result_label.pack()

status_label = tk.Label(root, text="")
status_label.pack()

# Run App
root.mainloop()
