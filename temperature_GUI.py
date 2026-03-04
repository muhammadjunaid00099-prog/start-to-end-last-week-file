import tkinter as tk
from tkinter import messagebox


def convert_temperature():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"Temperature in Celsius: {celsius:.2f}")
        
        
        if celsius > 50:
            message = "Temperature is Very Hot"
        elif celsius > 40:
            message = "Temperature is Hot"
        elif celsius > 30:
            message = "Temperature is Good"
        elif celsius > 20:
            message = "Temperature is Cold"
        else:
            message = "Temperature is Very Cold"
        
        messagebox.showinfo("Temperature Status", message)
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")


window = tk.Tk()
window.title("Fahrenheit to Celsius Converter")
window.geometry("400x200")


label = tk.Label(window, text="Enter temperature in Fahrenheit:")
label.pack(pady=10)


entry = tk.Entry(window, width=20)
entry.pack(pady=5)


convert_btn = tk.Button(window, text="Convert", command=convert_temperature)
convert_btn.pack(pady=10)


result_label = tk.Label(window, text="")
result_label.pack(pady=5)

window.mainloop()
