""" Shopping cart (model) for CP1200, Prac 11
    Lindsay Ward, 30/04/10, 19/05/13
"""

class Product(object):
    """ Product is a purchasable item """

    def __init__(self, name, price, taxable):
        self._name = name
        self._price = float(price)
        self._taxable = taxable

    def __str__(self):
        return self._name + " ($" + format(self._price, "0.2f") + ")"
    
    def setPrice(self, price):
        self._price = price

    def getPrice(self):
        return self._price

    def getName(self):
        return self._name

class Cart(object):
    """ Cart is a shopping cart that stores Products and financial details """
    # PRODUCTS is the list of available products
    # TODO: read this from file
    PRODUCTS = [Product("Apple", 1.2, False), Product("Fish", 13.85, False), Product("Ice Cream", 4.99, True), Product("Battery", 4.15, True)]

    def __init__(self):
        self._productList = [] 
        self._total = 0.0

    def __str__(self):
        display = ""
        for product in self._productList:
            display += product.__str__() + ", "
        display += "Total: $%0.2f" % self._total
        return display

    def addProduct(self, name):
        """ Add product by name """
        for product in Cart.PRODUCTS:
            if product._name == name:        
                self._productList.append(product)
                self._total += product.getPrice()
                return True
        return False

    def removeProduct(self, name):
        """ Remove product by name """
        for product in self._productList:
            if product._name == name:
                self._productList.remove(product)
                self._total -= product.getPrice()
                return True
        return False

    def getProducts(self):
        return self._productList

    def getTotal(self):
        return self._total


