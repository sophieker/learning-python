import tkinter as tk

bkcolor = input('What would you like the color of your sticky note to be? ')
nametitle = input('What would you like to title your sticky note? ')

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.configure(bg = bkcolor)
root.title(nametitle)

def callback():
    print ("click!")

b = tk.Button(root, text="B", command=callback)
b.pack()

canvas1.pack()

root.mainloop()
