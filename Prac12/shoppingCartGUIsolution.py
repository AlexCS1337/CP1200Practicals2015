"""
Luke Kennedy (CP1200 student in 2012)
GUI front end for Shopping Cart program
16/5/2012
"""

from tkinter import *
from shoppingCart import Product, Cart
DEBUG_MODE = True

class ShoppingProgram(Frame):
    """GUI Front-end to shopping cart program"""
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Shopping Cart")
        self.grid()

        #Initialise variables
        self.products = Cart.PRODUCTS
        self.entryList = []

        #Create Column Headers
        self.productHeaderLbl = Label(self, text="Products")
        self.productHeaderLbl.grid(row=0,column=0, sticky=W)
        self.priceHeaderLbl = Label(self, text="Price")
        self.priceHeaderLbl.grid(row=0, column=2, sticky=W)
        self.quantityHeaderLbl = Label(self, text="Quantity")
        self.quantityHeaderLbl.grid(row=0, column=4, sticky=W)

        #Create spacers for columns, since using width produces odd results
        self.spacer1Lbl = Label(self, text="", width=15)
        self.spacer1Lbl.grid(row=0, column=1)
        self.spacer2Lbl = Label(self, text="", width=10)
        self.spacer2Lbl.grid(row=0, column=3)

        #Create Product rows
        for count in range(len(self.products)):
            Label(self, text=self.products[count].getName()).grid(row=count+1, column=0, sticky=W)
            Label(self, text="$%0.2f" % self.products[count].getPrice()).grid(row=count+1, column=2, sticky=W)
            self.entryList.append(Entry(self, width=10))
            self.entryList[count].insert(0, "0")
            self.entryList[count].grid(row=count+1, column=4, sticky=W)

        #Create Total row
        self.updateBttn = Button(self, text="Update", command=self.updateTotal)
        self.updateBttn.grid(row=len(self.products)+1, column=0, sticky=W)
        self.totalLbl = Label(self, text="Total:")
        self.totalLbl.grid(row=len(self.products)+1, column=2, sticky=W)
        self.totalValue = Label(self, text="$0.00")
        self.totalValue.grid(row=len(self.products)+1, column=4, sticky=W)

    def updateTotal(self):
        """Calculates the total cost of the items and changes the relevant text field"""
        try:
            totalCost = 0
            for count in range(len(self.products)):
                totalCost += int(self.entryList[count].get()) * self.products[count].getPrice()
            self.totalValue["text"] = "$%0.2f" % totalCost
        except:
            if DEBUG_MODE:
               print("There was an error updating the total.")
        
            

if __name__ == "__main__":
    ShoppingProgram().mainloop()
