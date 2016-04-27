""" View & Controller for shopping cart - Text-only
    Lindsay Ward, 30/04/10, 10/05/12, 19/05/13
"""
from prac12shoppingCart import *

def test():
    """ Some quick tests to verify the Product and Cart classes, a bit """
    p1 = Product("Apple", 1.2, False)
    p2 = Product("Fish", 13.85, False)
    products = [p1, p2, Product("Ice Cream", 4.99, True), Product("Battery", 4.15, True)]
    cart = Cart()
    print(cart)
    for p in products:
        cart.addProduct(p.getName())
    cart.addProduct(p1.getName())
    cart.removeProduct("Fish")
    cart.addProduct(p2.getName())
    print(cart)

def main():
    """ Shopping program """
    cart = Cart()

    choice = menu()
    while choice != 4:
        if choice == 1:
            name = input("Product to add: ")
            # TODO: should check if product exists, output appropriate message
            cart.addProduct(name)
        elif choice == 2:
            name = input("Product to remove: ")
            # TODO: should check if product exists, output appropriate message
            cart.removeProduct(name)
        elif choice == 3:
            for p in cart.PRODUCTS:
                print(p)
        print("Your shopping cart is:")
        print(cart)
        
        choice = menu()

    print("That will be: $%0.2f" % cart.getTotal())
    print("Thank you for shopping with CP1200.")

def menu():
    """ print(a menu and get and return valid choice """
    print("1 - Add Product\n2 - Remove Product\n3 - List Products\n4 - Quit")
    choice = int(input(">>> "))
    while choice < 1 or choice > 4:
        print("1 - Add Product\n2 - Remove Product\n3 - List Products\4 - Quit")
        choice = int(input(">>> "))
    return choice

#test()
main()
