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

volt_slider = Scale(root, from_= 9, to= 0.1, resolution=0.1)
volt_slider.grid(row = 10, column = 10)
resistance_slider = Scale(root, from_=1000, to=10, resolution=0.1)
resistance_slider.grid(row = 20, column = 10)

root.mainloop()


# calculating current
v = int(input("voltage: "))
r = int(input("Enter resistance: "))
i = v/r
