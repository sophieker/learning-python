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

voltage = 0
resistance = 1
current = 0

# update displays
def update_battery():
    print("Number of batteries: ", math.floor(voltage/1.5))
    
def update_resistor():
    print("Number of dots: ", math.floor(resistance/10))

def update_wire():
    print("current: ", current)

# update circuit 
def update_voltage(volt_num):
    print("volt_num: >", volt_num, "<")
    voltage = float(volt_num)
    update_battery()
    update_current()

def update_resistance(resistance_num):
    resistance = float(resistance_num.get())
    update_resistor()
    update_current()

def update_current():
    current = (voltage * 1000)/resistance
    update_wire()
    

# creating sliders
volt_num = DoubleVar()
volt_slider = tk.Scale(root, from_= 0.1, to= 9, resolution=0.1, orient=HORIZONTAL, variable = volt_num, command = update_voltage)
volt_slider.place(x = 150, y = 600, height = 200, width = 200)

resistance_num = DoubleVar()
resistance_slider = tk.Scale(root, from_=10, to=1000, resolution=0.1, orient=HORIZONTAL, variable = resistance_num, command = update_resistance)
resistance_slider.place(x = 450, y = 600, height = 200, width = 200)

battery = []

# labels for sliders
volt_label = tk.Label(root, text = "voltage (V)")
volt_label.place(x = 140, y = 650)
resistance_label = tk.Label(root, text = "resistance (Ω)")
resistance_label.place(x = 440, y = 650)

# draw shapes
circuit = c.create_rectangle(150, 150, 650, 500, width = 7)
c.pack()

resistance_rect = c.create_rectangle(200, 470, 600, 530, fill= 'white', width=2)
c.pack()
    

# calculating current
"""
update_voltage(volt_num)
update_resistance(resistance_num)
update_current()
"""
root.mainloop()

"""
- draw rectangles (batteries that increase with voltage, box with increasing particles as resistance increases
- display the current, voltage, and resistance
- figure out how to get value of scale
- toggle show equation
"""
