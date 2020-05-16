#imports
import tkinter as tk
from tkinter import *
from tkinter.font import Font
import tkinter.filedialog, tkinter.messagebox
import os
from os import system

#beginning questions
family = (input('What font would you like to use? ') or "Arial")
nametitle = input('What would you like to title your sticky note? ')
size = "12"

#main window
root = tk.Tk()
root.title(nametitle)
root.geometry("300x300")

c = tk.Canvas(root, width = 300, height = 300)

#font counters
bold_font_count = 0
italic_font_count = 0
underline_font_count = 0
overstrike_font_count = 0


#set font
myFont = Font(family = family, size=size)
myFontbold = Font(family = family, size=size, weight = "bold")
myFontitalic = Font(family = family, size=size, slant = "italic")
myFontunderline = Font(family = family, size=size, underline = 1)
myFontoverstrike = Font(family = family, size=size, overstrike = 1)

#create main text window and default text
t = tk.Text(root, font = myFont, height=20, width=40)
t.insert(INSERT, "Type text here.....")
t.pack()

#define commands
def changefont():
    family = (input('What would you like to change your font to? '))
    myFont.configure(family = family)

def changesize():
    size_temp = (input('What size font would you like to use? '))
    size = size_temp
    myFont.configure(size = size)
    myFontbold.configure(size = size)
    myFontitalic.configure(size = size)
    myFontunderline.configure(size = size)
    myFontoverstrike.configure(size = size)


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

#save text widget

class TextWidget:
    def __init__(self, text):
        self.text = text # pass the text widget
        self.filename = ''
        self._filetypes = [
        ('Text', '*.txt'),
            ('All files', '*'),
            ]

    def save_file(self, whatever = None):
        if (self.filename == ''):
            self.save_file_as()
        else:
            f = open(self.filename, 'w')
            f.write(self.text.get('1.0', 'end')) # change every 'self' that refers to the Text, to self.text
            f.close()
            tkinter.messagebox.showinfo('FYI', 'File Saved.')

    def save_file_as(self, whatever = None):
        self.filename = tkinter.filedialog.asksaveasfilename(defaultextension='.txt',
                                                             filetypes = self._filetypes)
        f = open(self.filename, 'w')
        f.write(self.text.get('1.0', 'end'))
        f.close()
        tkinter.messagebox.showinfo('FYI', 'File Saved')

    def open_file(self, whatever = None, filename = None):
        if not filename:
            self.filename = tkinter.filedialog.askopenfilename(filetypes = self._filetypes)
        else:
            self.filename = filename
        if not (self.filename == ''):
            f = open(self.filename, 'r')
            f2 = f.read()
            self.text.delete('1.0', 'end')
            self.text.insert('1.0', f2)
            f.close()
            self.text.title('Sticky %s)' % self.filename)

#on off font change 
def boldtext():
    t.tag_add("boldtexttag", "sel.first", "sel.last")
    global bold_font_count
    bold_font_count = bold_font_count + 1
    if (bold_font_count % 2) == 0:
        t.tag_configure("boldtexttag", font = myFont)
    else:
        t.tag_configure("boldtexttag", font = myFontbold)

def italictext():
    t.tag_add("italictexttag", "sel.first", "sel.last")
    global italic_font_count
    italic_font_count = italic_font_count + 1
    if (italic_font_count % 2) == 0:
        t.tag_configure("italictexttag", font = myFont)
    else:
        t.tag_configure("italictexttag", font = myFontitalic)
    
def underlinetext():
    t.tag_add("underlinetexttag", "sel.first", "sel.last")
    global underline_font_count
    underline_font_count = underline_font_count + 1
    if (underline_font_count % 2) == 0:
        t.tag_configure("underlinetexttag", font = myFont)
    else:
        t.tag_configure("underlinetexttag", font = myFontunderline)
    
def overstriketext():
    t.tag_add("overstriketexttag", "sel.first", "sel.last")
    global overstrike_font_count
    overstrike_font_count = overstrike_font_count + 1
    if (overstrike_font_count % 2) == 0:
        t.tag_configure("overstriketexttag", font = myFont)
    else:
        t.tag_configure("overstriketexttag", font = myFontoverstrike)
    

    

#menu bar
menubar = tk.Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="New", command = donothing)
filemenu.add_command(label = "Open", command = open_file)
filemenu.add_command(label = "Save", command = save_file)
filemenu.add_command(label = "Save as...", command = save_file_as)

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
fontmenu.add_command(label = "Italic", command = italictext)
fontmenu.add_command(label = "Size", command = changesize)
fontmenu.add_command(label = "Underline", command = underlinetext)
fontmenu.add_command(label = "Overstrike", command = overstriketext)

fontmenu.add_separator()

fontmenu.add_command(label = "Change font", command = changefont)




root.config(menu = menubar)

#end 

c.pack()

root.mainloop()



