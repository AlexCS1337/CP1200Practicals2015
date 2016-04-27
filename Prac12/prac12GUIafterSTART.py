""" CP1200 GUI program, using after to control execution. Trevor Andersen & Lindsay Ward, April 2010 
Modify this program to include a start and a stop button to start and stop the timer.
Then add a reset button and a quit button as well.
"""
from tkinter import *

DELAY = 100 # 100 = 100/1000s of a second (0.1 seconds)

class Application(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.labelCount = Label(self, text='0')
        self.labelCount.grid()
        # buttons to start/stop with callback functions registered
        self.buttonStart = Button(self, text="Start", command=self.start)
        self.buttonStart.grid()
        # ...
        
        # Here is the after method, specifying which function to call after how long
        # run update after DELAY ms
        self.after(DELAY, self.update)

    def update(self):
        self.labelCount["text"] = str(int(self.labelCount["text"]) + 1)
        self.after(DELAY, self.update)

    def start(self):
        self.update()
        
app = Application()
app.mainloop()
