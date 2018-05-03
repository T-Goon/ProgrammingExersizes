from tkinter import *

master = Tk()

w = Canvas(master, width=400, height=400)
w.pack()

# Head
w.create_oval(20, 20, 380, 380, fill="yellow", width=3)

# Eyes
w.create_oval(100, 100, 150, 150, fill="black")
w.create_oval(250, 100, 300, 150, fill="black")

# Nose
w.create_line(200, 175, 230, 225, width=3)
w.create_line(230, 225, 210, 225, width=3)

# Mouth
w.create_line(100, 275, 300, 275, width=3)

mainloop()
