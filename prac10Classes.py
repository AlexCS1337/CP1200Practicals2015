'''
CP1200 Practical 10 Solutions - Classes

Created on 11/02/2014

@author: Lindsay Ward
'''
from car import Car

# Cars
# Write a line of code for each of the following:
# 1.    Create a Car object called "limo" with 100 units of fuel.
# 2.    Add 20 more units of fuel to the car.
# 3.    Display the amount of fuel in the car.
# 4.    Attempt to drive the car 115km.
# 5.    Display the car's odometer reading.

# limo = Car(100)
# limo.addFuel(20)
# print(limo.getFuel())
# limo.drive(115)
# print(limo.getOdometer())
# print(limo)

# Playing With Cars

MENU = "Menu:\nd) drive\nr) refuel\nq) quit"

def main():
    # create an instance of a Car with an initial fuel value of 100
    car = Car(100)
    
    print("Let's drive!")
    print(car)
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "d":
            distanceToDrive = int(input("How many km do you wish to drive? "))
            distanceDriven = car.drive(distanceToDrive)
            print("The car drove " + str(distanceDriven) + "km", end="")
            if car.getFuel() == 0:
                print(" and ran out of fuel", end="")
            print(".")
        elif choice == "r":
            fuelToAdd = int(input("How many units of fuel do you want to add to the car? "))
            while fuelToAdd < 0:
                print("Fuel amount must be >= 0")
                fuelToAdd = int(input("How many units of fuel do you want to add to the car? "))
            car.addFuel(fuelToAdd)
            print("Added", fuelToAdd, "units of fuel.")
        else:
            print("Invalid choice")
        print()
        print(car)
        print(MENU)
        choice = input("Enter your choice: ").lower()
    print("\nGood bye!")

main()






