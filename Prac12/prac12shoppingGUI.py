__author__ = 'Smoo'


from tkinter import *
from prac12shoppingCart import *

class Application(Frame):
    def ___init__(self):
        Frame.__init__(self)
        self.master.title("Shopping GUI")
        self.master["bg"] = "blue"
        self["bg"] = "white"
        self.grid()



Application().mainloop()
