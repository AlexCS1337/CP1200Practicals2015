""" GUI example for CP1200 
    Lindsay Ward, 30/04/2010
"""

from tkinter import *
from random import randint

class Application(Frame):
    """ Demo GUI application """
    def __init__(self):
        Frame.__init__(self)
        self.master.title("CP1200 GUI")
        self.master["bg"] = "pink"
        self["bg"] = "white"
        self.grid()
        self.bttn_clicks = 0    # number of clicks

# We can just create widgets directly here 

        #Create the click button
        self.bttn = Button(self)
        self.bttn["text"] = "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid(row = 0, column = 0)

        # Create the reset button - shortcut way
        self.resetBttn = Button(self, text = "Reset", command = self.reset).grid(row = 0, column = 1)

        #Create the text label and text field
        self.titleLbl = Label(self, text = "Title:", fg = "blue", bg = "yellow")
        self.titleLbl.grid(row = 2, column = 0, sticky=W)
        self.textEntry = Entry(self)
        self.textEntry.grid(row = 2, column = 1)

        #Create the button for setting the title
        self.titleBttn = Button(self, text = "Set Title", command = self.setTitle)
        self.titleBttn.grid(row = 3, column = 0, columnspan = 2)

        #Colour text fields and set button
        self.colourRLbl = Label(self, text = "Colour: ").grid(row = 4, column = 0)
        self.colourEntry = Entry(self)
        self.colourEntry.grid(row = 4, column = 1)
        self.colourBttn = Button(self, text = "Set Colour", command = self.setColour)
        self.colourBttn.grid(row = 7, column = 0)
        self.colourRandBttn = Button(self, text = "Random Colour", command = self.randColour)
        self.colourRandBttn.grid(row = 7, column = 1)

        #Check boxes for food likes
        self.likesFood1 = BooleanVar()
        self.likesFood2 = BooleanVar()
        Checkbutton(self, text = "Pizza", variable = self.likesFood1, command = self.updateLikes).grid(row=8, column=0) 
        Checkbutton(self, text = "Pasta", variable = self.likesFood2, command = self.updateLikes).grid(row=8, column=1) 
        self.likesText = Text(self, width = 30, height = 1, wrap = WORD)
        self.likesText.grid(row = 9, column = 0, columnspan = 2)
        
    def update_count(self):
        """ Update the count """
        self.bttn_clicks += 1
        self.bttn["text"]="Total Clicks: "+ str(self.bttn_clicks)

    def reset(self):
        """ Reset the click count and title """
        self.bttn_clicks = 0
        self.bttn["text"]="Total Clicks: "+ str(self.bttn_clicks)
        self.master.title("CP1200 GUI")

    def setTitle(self):
        self.master.title(self.textEntry.get())

    def setColour(self):
        self["bg"] = self.colourEntry.get()
        #print self.colourR.get()

    def randColour(self):
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        randColour = "#" + hex(r)[2:] + hex(g)[2:] + hex(b)[2:]
        while len(randColour) < 7:
            randColour += str(randint(0,9))
        self["bg"] = randColour

    def updateLikes(self):
        message = "You like "
        if self.likesFood1.get() and self.likesFood2.get():
            message += "Pizza and Pasta"
        elif self.likesFood1.get():
            message += "Pizza"
        elif self.likesFood2.get():
            message += "Pasta"
        else:
            message += "nothing!"
#        print(self.likesFood1.get(), self.likesFood2.get(), message)
        self.likesText.delete(0.0, END)
        self.likesText.insert(0.0, message)
    
# Create an instance of the application and start responding to events            
Application().mainloop()
