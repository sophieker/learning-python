from tkinter import *

root = Tk()
root.geometry("300x300")

mb = tk.Menubutton(root, text="menu1")
mb.menu = Menu(mb)
mb["menu"] = mb.menu

mb.menu.add_command(label="Option 1", command=lambda: print("This is option 1")
mb.menu.add_command(label="Option 2", command=lambda: print("This is option 2")

mb.pack()

root.mainloop()
