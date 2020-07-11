import turtle as t
import tkinter as tk
from tkinter import *
from turtle import *
import tkinter.font as tkFont
import math
import random

# initializing window
root = tk.Tk()
root.title("ohm's law simulation")
root.geometry("800x700")

# font preset
bold_font = tkFont.Font(family="Helvetica", size=30, weight="bold")

c = tk.Canvas(root, width = 800, height = 700)

voltage_ = 0
resistance_ = 0.1

# update displays
def update_battery(voltage):
    print("Number of batteries: ", math.floor(voltage/1.5))
    battery_num = math.floor(voltage/1.5)
    
def update_resistor(resistance):
    num_dots = math.floor(resistance/5)
    for i in dots:
        c.delete(i)
    for i in range (num_dots):
        startx = random.randrange(205, 595)
        starty = random.randrange(475, 525)
        oval = c.create_oval(startx, starty, startx + 3, starty + 3, fill="red", outline = "red")
        dots.append(oval)



def update_wire(current):
    print("current: ", current)
    # current_display = c.create_text(370, 300, font=bold_font, text=str(current))
    # c.pack()

# update circuit 
def update_voltage(volt_num):
    global voltage_
    print("volt_num: >", volt_num, "<")
    voltage = float(volt_num)
    voltage_ = voltage
    update_battery(voltage)
    update_current()

def update_resistance(resistance_num):
    global resistance_
    print("resistance_num: >", resistance_num, "<")
    resistance = float(resistance_num)
    resistance_ = resistance
    update_resistor(resistance)
    update_current()

def update_current():
    print("update current: ", voltage_, resistance_)
    current = (voltage_ * 1000)/resistance_
    update_wire(current)
    
# creating sliders
volt_num = DoubleVar()
volt_slider = tk.Scale(root, from_= 0.1, to= 9, resolution=0.1, orient=HORIZONTAL, variable = volt_num, command = update_voltage)
volt_slider.place(x = 150, y = 600, height = 200, width = 200)

resistance_num = DoubleVar()
resistance_slider = tk.Scale(root, from_=10, to=1000, resolution=0.1, orient=HORIZONTAL, variable = resistance_num, command = update_resistance)
resistance_slider.place(x = 450, y = 600, height = 200, width = 200)

battery = []
dots = []
# current_display = c.create_text(370, 300, font=bold_font, text="0")
# c.pack()


# labels for sliders
volt_label = tk.Label(root, text = "voltage (V)")
volt_label.place(x = 140, y = 650)
resistance_label = tk.Label(root, text = "resistance (Ω)")
resistance_label.place(x = 440, y = 650)

# draw shapes
circuit = c.create_rectangle(150, 150, 650, 500, width = 10)
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
- draw rectangles (batteries that increase with voltage)
- display the current
- toggle show equation
- white particles to show current
"""
