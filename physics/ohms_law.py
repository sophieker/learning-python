import turtle as t
import tkinter as tk
from tkinter import *
from turtle import *
import tkinter.font as tkFont
import math
import sys

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
def toggle():
    if mylabel.visible:
        btnToggle["text"] = "Show equation"
        mylabel.place_forget()
    else:
        mylabel.place(mylabel.pi)
        btnToggle["text"] = "Hide equation"
    mylabel.visible = not mylabel.visible

mylabel_font = tkFont.Font(family = "Lucida Grande", size=30)
mylabel = tk.Label(root, text="V = IR", font=mylabel_font)
mylabel.visible = True
mylabel.place(x=400, y=50)
mylabel.pi = mylabel.place_info()

btnToggle = tk.Button(root, text="Hide equation", command=toggle)
btnToggle.place(x=600, y=50)
"""

# draw shapes
circuit = c.create_rectangle(150, 150, 650, 500, width = 7)
c.pack()

resistance_rect = c.create_rectangle(200, 470, 600, 530, fill= 'white', width=2)
c.pack()

root.mainloop()


# calculating current
v = int(input("voltage: "))
r = int(input("Enter resistance: "))
i = (v*1000)/r

"""
- draw rectangles (batteries that increase with voltage, box with increasing particles as resistance increases
- display the current, voltage, and resistance
- figure out how to get value of scale
- toggle show equation
"""
