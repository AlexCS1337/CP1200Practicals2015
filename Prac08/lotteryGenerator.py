__author__ = 'Smoo'


import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

if NUMBERS_PER_LINE < (MAXIMUM - MINIMUM):
    quickPicks = int(input("How many quick picks? "))
    while quickPicks < 0:
        print("That makes no sense!")
        quickPicks = int(input("How many quick picks? "))

    for i in range(quickPicks):
        drawNumbers = []
        for i in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in drawNumbers:
                number = random.randint(MINIMUM, MAXIMUM)
            drawNumbers.append(number)

        drawNumbers.sort()
        for number in drawNumbers:
            print(format(number, "2d"), end="")
        print()