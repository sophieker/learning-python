import tkinter as tk
from tkinter import *
from tkinter.font import Font

family = (input('What font would you like to use? ') or "Arial")
nametitle = input('What would you like to title your sticky note? ')

root = tk.Tk()
root.title(nametitle)
root.geometry("400x400")

c = tk.Canvas(root, width = 300, height = 300)
myFont = Font(family = family, size=12)

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
menubar = tk.Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="New", command = donothing)
filemenu.add_command(label = "Open", command = donothing)
filemenu.add_command(label = "Save", command = donothing)
filemenu.add_command(label = "Save as...", command = donothing)
filemenu.add_command(label = "Close", command = donothing)

filemenu.add_separator()

filemenu.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label = "Undo", command = donothing)

editmenu.add_separator()

editmenu.add_command(label = "Cut", command = donothing)
editmenu.add_command(label = "Copy", command = donothing)
editmenu.add_command(label = "Paste", command = donothing)
editmenu.add_command(label = "Delete", command = donothing)
editmenu.add_command(label = "Select All", command = donothing)

menubar.add_cascade(label = "Edit", menu = editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "Help Index", command = donothing)
helpmenu.add_command(label = "About...", command = donothing)
menubar.add_cascade(label = "Help", menu = helpmenu)

root.config(menu = menubar)



def callback():
    myFont.configure(weight = "bold")
    t.configure(font = myFont)
    
b = tk.Button(root, text="BOLD", command=callback)
b.pack()


t = tk.Text(root, font = myFont, height=30, width=40)
t.insert(INSERT, "Type text here.....")
t.pack()

c.pack()

root.mainloop()
