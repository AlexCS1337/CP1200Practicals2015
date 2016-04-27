__author__ = 'Smoo'


from car import Car

MENU = "Menu:\nd) drive\nr) refuel\nq) quit"

def main():
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