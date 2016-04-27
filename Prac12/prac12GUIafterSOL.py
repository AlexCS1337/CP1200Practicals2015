""" CP1200 Practical 12 solution - 
GUI program, using after to control execution. 
Trevor Andersen & Lindsay Ward, 
Started: April 2010 
Last modified: May 2014 """
from tkinter import *

DELAY = 100 # 100 = 100/1000s of a second (0.1 seconds)

class Application(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        # create a stringVar and associate it with the label used to display it
        self.countStr = StringVar()
        self.countStr.set('1')
        self.labelCount = Label(self, textvariable=self.countStr)
        self.labelCount.grid()
        # buttons to start/stop with callback functions registered
        self.buttonStart = Button(self, text="Start", command=self.start)
        self.buttonStart.grid()
        self.buttonStop = Button(self, text="Stop", command=self.stop)
        self.buttonStop.grid()
        # Boolean for controlling whether counting is on or not
        self.isCounting = False 
        # Here is the after method, specifying which function to call after how long
        # run update after DELAY ms
        self.after(DELAY, self.update)

    def update(self):
        if self.isCounting:
            # update the stringVar associated with the label by 1
            self.countStr.set(str(int(self.countStr.get()) + 1))
            # technique to use if just using the contents of label, not a StringVar
#             self.labelCount["text"] = str(int(self.labelCount["text"]) + 1)

        # call update again after DELAY ms... 
        # note this does not call it from inside update. It's not recursion. 
        self.after(DELAY, self.update)

    def start(self):
        self.isCounting = True
        
    def stop(self):
        self.isCounting = False
        
app = Application()
app.mainloop()
