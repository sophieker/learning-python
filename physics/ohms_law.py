import turtle as t
import tkinter as tk
from tkinter import *
from turtle import *
import math

# initializing window
root = tk.Tk()
root.title("ohm's law simulation")
root.geometry("800x700")

c = tk.Canvas(root, width = 800, height = 700)

# creating sliders
volt_slider = tk.Scale(root, from_= 0.1, to= 9, resolution=0.1, orient=HORIZONTAL)
volt_slider.place(x = 150, y = 600, height = 200, width = 200)
resistance_slider = tk.Scale(root, from_=10, to=1000, resolution=0.1, orient=HORIZONTAL)
resistance_slider.place(x = 450, y = 600, height = 200, width = 200)

# labels for sliders
volt_label = tk.Label(root, text = "voltage")
volt_label.place(x = 140, y = 650)
resistance_label = tk.Label(root, text = "resistance")
resistance_label.place(x = 440, y = 650)

# toggle equation
"""
equation_check_var = IntVar()
equation_check = tk.Checkbutton(root, text = "display equation", variable = equation_check_var, onvalue = 1, offvalue = 0)
equation_check.place(x = 600, y = 50)

if equation_check_var == 1:
    equation = tk.Label(root, text = "V = IR", family = "Lucida Grande", size=20)
    equation.place(x = 400, y = 50)

"""

root.mainloop()


# calculating current
v = int(input("voltage: "))
r = int(input("Enter resistance: "))
i = v/r

"""
- create window
- draw rectangles (wire, batteries that increase with voltage,
box with increasing particles as resistance increases
- display the current, voltage, and resistance
- figure out how to get value of scale
- button to calculate current
"""
