#imports
import tkinter as tk
from tkinter import *
from tkinter.font import Font

#beginning questions
family = (input('What font would you like to use? ') or "Arial")
nametitle = input('What would you like to title your sticky note? ')

#main window
root = tk.Tk()
root.title(nametitle)
root.geometry("300x300")

c = tk.Canvas(root, width = 300, height = 300)

#font counters
bold_font_count = 0

#set font
myFont = Font(family = family, size=12)

#define commands
def changefont():
    family = (input('What would you like to change your font to? '))
    myFont.configure(family = family)
    


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def boldtext():
    bold_font_count = bold_font_count + 1
    if (bold_font_count % 2) == 0:
        myFont.configure(weight = "normal")
        t.configure(font = myFont)
    else:
        myFont.configure(weight = "bold")
        t.configure(font = myFont)

#menu bar
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

fontmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Font", menu = fontmenu)
fontmenu.add_command(label = "Bold", command = boldtext)
fontmenu.add_command(label = "Italic", command = donothing)
fontmenu.add_command(label = "Size", command = donothing)
fontmenu.add_command(label = "Underline", command = donothing)
fontmenu.add_command(label = "Italic", command = donothing)
fontmenu.add_command(label = "Highlight", command = donothing)

fontmenu.add_separator()

fontmenu.add_command(label = "Change font", command = changefont)




root.config(menu = menubar)

#end and default text

t = tk.Text(root, font = myFont, height=20, width=40)
t.insert(INSERT, "Type text here.....")
t.pack()

c.pack()

root.mainloop()
