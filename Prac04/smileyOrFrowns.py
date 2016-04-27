__author__ = 'Smoo'

totalOfSmileys = 0
totalOfFrowneys = 0
count = 0

#Display the menu
MENU = "\nMenu:\n(S)miley\n(F)rowney\n(Q)uit"
print(MENU)

#Get the choice
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "S":
        print(":)")
        totalOfSmileys += 1
    elif choice == "F":
        print(":(")
        totalOfFrowneys += 1
    else:
        print("Invalid menu choice.")
    print(MENU)
    choice = input(">>> ").upper()
print ("There has been", totalOfSmileys, "smileys and", totalOfFrowneys, "frowneys.")