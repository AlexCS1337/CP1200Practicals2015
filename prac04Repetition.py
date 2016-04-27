'''
CP1200 Prac 04 Solutions - Repetition
Created on 11/02/2014

@author: Lindsay Ward
'''


# Quick exercise
repetitions = int(input("How many numbers do you want to add up? "))
total = 0
for i in range(repetitions):
    number = int(input("Enter number " + str(i + 1) + ": "))
    total += number
print("The total of those", repetitions, "numbers is", total)


# Menu-driven program, smiley/frowny, including counting
"""
Following the general pattern of a menu-driven program, as follows:

display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else
        display invalid input error message
    display menu
    get choice

"""
MENU = "    (S)miley\n    (F)rowny\n    (Q)uit"
SMILEY = ":)"
FROWNY = ":("
smileysChosen = 0
frowniesChosen = 0

print(MENU)
choice = input(">>> ").upper()  # this converts the input to uppercase, which is useful for the ifs
while choice != "Q":
    if choice == "S":
        print(SMILEY)
        smileysChosen += 1
    elif choice == "F":
        print(FROWNY)
        frowniesChosen += 1
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper() 
print("Farewell", SMILEY)
print("You chose", smileysChosen, "smileys, and", frowniesChosen, "frownies.")
# Note: we could improve this by using singular words - e.g. "1 smiley"


# Calculating Running Totals
# 2. Problem C
SECRET = 'a'
guesses = 1  # Start at 1 because the last guess (not inside the loop) will always be correct, so this accounts for it
guess = input("Guess letter: ")
while guess != SECRET:
    print("That's not it.")
    guesses += 1
    guess = input("Guess letter: ")
print("You got it in", guesses, "guesses!")




# Error-checking Loops
# 2. Problem A
def printCurrency(value):
   print("$" + format(value, '.2f'))

workerLevel = int(input("Worker level: "))
while workerLevel < 1 or workerLevel > 10:
    print("Error. Please enter a number between 1 and 10.")
    workerLevel = int(input("Worker level: "))
# We know we have a valid input 1-10.
print("You salary is: ", end="")
printCurrency(workerLevel * 5000)


# Error-checking Loops
# 2. Problem B
# note this is case-sensitive (but a bit insensitive when it comes to the error message)
choice = input("on or off?")
while choice != "on" and choice != "off": 
    print("What part of this don't you understand?")
    choice = input("on or off?")
print("The light is", choice)

# Extension 2 - Fahrenheit to/from Celsius
# Note that the interface (displayed text) is not very user-friendly

MENU = "C (for C to F conversion)\nF (the opposite)\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(format(fahrenheit, '.2f'))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(format(celsius, '.2f'))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
