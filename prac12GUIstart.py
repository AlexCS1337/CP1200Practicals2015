""" GUI example for CP1200 
    Lindsay Ward, 30/04/2010, 19/05/2013
"""

from tkinter import *

class Application(Frame):
    """ Demo GUI application for CP1200 Practical """
    def __init__(self):
        Frame.__init__(self)
        self.master.title("CP1200 GUI")
        self.master["bg"] = "pink"
        self["bg"] = "white"
        self.grid()
        self.button_clicks = 0    # number of clicks

# We can just create widgets directly here 
        #Create the click button
        self.countButton = Button(self)
        self.countButton["text"] = "Total Clicks: 0"
        self.countButton["command"] = self.update_count
        self.countButton.grid(row=0, column=0)

        # Create the reset button - shortcut way: anonymous object
        Button(self, text="Reset", command=self.reset).grid(row=0, column=1)

        #Create the text label and text field
        Label(self, text="Title:", fg="blue", bg="yellow").grid(row=2, column=0, sticky=W)
        self.textEntry = Entry(self)
        self.textEntry.grid(row=2, column=1)

    def update_count(self):
        """ Update the count """
        self.button_clicks += 1
        self.countButton["text"]="Total Clicks: "+ str(self.button_clicks)

    def reset(self):
        """ Reset the click count and title """
        self.button_clicks = 0
        self.countButton["text"] = "Total Clicks: "+ str(self.button_clicks)
        self.master.title("CP1200 GUI")

# Create an instance of the application and start responding to events            
Application().mainloop()
