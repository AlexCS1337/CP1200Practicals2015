__author__ = 'Smoo'


def displayOdds():
    maximum = int(input("Enter the maximum value to display: "))
    for i in range(1, maximum + 1, 2):
        print(i, end=" ")

def displayEvens():
    maximum = int(input("Enter the maximum value to display: "))
    for i in range(2, maximum + 1, 2):
        print(i, end=" ")

def displayReciprocals():
    maximum = int(input("Enter the maximum value to display: "))
    for i in range(1, maximum +1):
        print(format(1/i, ".6f"), end=" ")

#Display the menu
MENU = "\nMenu:\n(o)dds\n(e)vens\n(r)eciprocals\n(q)uit"
print(MENU)

#Get the choice
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "O":
        displayOdds()
    elif choice == "E":
        displayEvens()
    elif choice == "R":
        displayReciprocals()
    else:
        print("Invalid menu choice.")
    print(MENU)
    choice = input(">>> ").upper()