

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

        Button(self, text="Set Title", command=self.set_title).grid(row=3, column=1)
        self.textEntry.get()

        Label(self, text="Colour:", fg="black", bg="white").grid(row=4, column=0, sticky=W)
        self.textEntry = Entry(self)
        self.textEntry.grid(row=4, column=1)


        Button(self, text="Set Colour", command=self.set_colour).grid(row=5, column=0)
        self.colour.TextEntry.get()

        Button(self, text="Random Colour").grid(row=5, column=1)

        self.likes_pizza = BooleanVar()
        Checkbutton(self, text= "Pizza",
                    variable = self.likes_pizza,
                    command = self.update_text).grid(row=6, column=0, sticky=W)

        self.likes_pasta = BooleanVar()
        Checkbutton(self, text= "Pasta",
                    variable = self.likes_pasta,
                    command = self.update_text).grid(row=6, column=1, sticky=W)



    def update_text(self):
        likes = ""
        if self.likes_pizza.get():
            likes += "You like pizza"
        elif self.likes_pasta.get():
            likes += "You like pasta"


    def update_count(self):
        """ Update the count """
        self.button_clicks += 1
        self.countButton["text"]="Total Clicks: "+ str(self.button_clicks)


    def reset(self):
        """ Reset the click count and title """
        self.button_clicks = 0
        self.countButton["text"] = "Total Clicks: "+ str(self.button_clicks)
        self.master.title("CP1200 GUI")


    def set_title(self):
        self.master.title("")


    def set_colour(self):
        self["bg"] =

# Create an instance of the application and start responding to events            
Application().mainloop()
