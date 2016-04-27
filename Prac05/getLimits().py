__author__ = 'Smoo'


from random import randint, uniform


def getLimits():
    lowestNumber = int(input("Enter the minimum: "))
    prompt = int(input("Enter the maximum(" + str(lowestNumber) + " or above):"
    highestNumber = int(input(prompt))
    while highestNumber < lowestNumber:
        print("Maximum too low!")
        highestNumber = int(input(prompt))
    return lowestNumber, highestNumber

getLimits()