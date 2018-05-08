from tkinter import *

class App:

    # Contructor
    def __init__(self, master):
        
        frame = Frame(master)
        frame.pack()
        
        # Exit Button
        self.button = Button(frame, text="Exit",
        fg = "blue", command = frame.quit)
        self.button.pack(side = RIGHT)
        
        # Prints 'hi!' to console 
        self.hiThere = Button(frame, text="HI", command = self.say_hi)
        self.hiThere.pack(side = LEFT)

    # Function that prints something
    def say_hi(self):
        print("hi！")

# Create Tk object and pass it into the 'App' class
root = Tk()
app = App(root)

# Enter Tk event loop and destroys main window
root.mainloop()

# May be unneeded
root.destroy()
