import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import math
import random

# ---initializing window
root = tk.Tk()
root.title("ohm's law simulation")
root.geometry("800x700")

# ---font preset
bold_font = tkFont.Font(family="Helvetica", size=30, weight="bold")

c = tk.Canvas(root, width = 800, height = 700)

voltage_ = 0.0
resistance_ = 10.0


# ---update displays
def update_battery(voltage):
    # start batt from: x 180, y 135
    # batt height: 30
    # batt width: 50
    # batt label: 1.5 V
    battery_num = math.floor(voltage / 1.5)
    for i in battery_labels:
        c.delete(i)
    for i in battery:
        c.delete(i)
    # for i in battery_remainder:
    #    c.delete(i)
    for i in range(battery_num):
    #    if voltage%1.5 != 0:
    #        batt_remainder = c.create_text(245 + i * 51, 130, text=round(voltage%1.5, 2))
    #        battery_remainder.append(batt_remainder)
        batt = c.create_rectangle(180 + i * 51, 135, (180 + i * 51) + 50, 165, fill = "white", width=2)
        battery.append(batt)
        batt_label = c.create_text(205 + i * 51, 150, text="1.5 V")
        battery_labels.append(batt_label)

    
def update_resistor(resistance):
    num_dots = math.floor(resistance/5)
    random.seed(10)
    for i in resistance_dots:
        c.delete(i)
    for i in range (num_dots):
        startx = random.randrange(205, 595)
        starty = random.randrange(475, 525)
        oval = c.create_oval(startx, starty, startx + 3, starty + 3, fill="red", outline = "red")
        resistance_dots.append(oval)



def update_wire(current):
    num_current = current * 10
    print("current: ", current)
    for i in current_display:
        c.delete(i)
    for i in current_dots:
        c.delete(i)
    current_display_temp = c.create_text(400, 320, font=bold_font, text=str(round(current, 2)))
    current_display.append(current_display_temp)
    for i in range(current_dots):
        startx_left = 
        startx_right =
        starty_left =
        starty_right =


# ---update circuit
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


# ---creating sliders
volt_num = DoubleVar()
volt_slider = tk.Scale(root, from_= 0.1, to= 9, resolution=0.1, orient=HORIZONTAL, variable = volt_num, command = update_voltage)
volt_slider.place(x = 150, y = 600, height = 200, width = 200)

resistance_num = DoubleVar()
resistance_slider = tk.Scale(root, from_=10, to=1000, resolution=0.1, orient=HORIZONTAL, variable = resistance_num, command = update_resistance)
resistance_slider.place(x = 450, y = 600, height = 200, width = 200)

battery = []
battery_labels = []
# battery_remainder = []
resistance_dots = []
current_display = []
current_dots = []
current_display_init = c.create_text(400, 320, font=bold_font, text="10.0")
current_display.append(current_display_init)


# ---labels for sliders
volt_label = tk.Label(root, text = "voltage (V)")
volt_label.place(x = 140, y = 650)
resistance_label = tk.Label(root, text = "resistance (Ω)")
resistance_label.place(x = 440, y = 650)

# ---draw shapes
circuit = c.create_rectangle(150, 150, 650, 500, width = 15)
c.pack()

resistance_rect = c.create_rectangle(200, 470, 600, 530, fill= 'white', width=2)
c.pack()

circuit_units = tk.Label(root, text = "mA", font = ("Helvetica", 16))
circuit_units.place(x = 385, y = 340)

#---equation
equation = tk.Label(root, text = "V = IR", font = ("Times", 30))
equation.place(x=355, y=70)
    

# calculating current
"""
update_voltage(volt_num))
update_resistance(resistance_num)
update_current()
"""
root.mainloop()

"""
- toggle show equation
- white particles to show current
- increasing size of batteries or some display of how much left until new battery
"""
