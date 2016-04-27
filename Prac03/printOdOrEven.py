__author__ = 'Smoo'


# number = int(input("Enter a number: "))
# if number < 0:
# print(number, "is negative")
# else:
#     print(number, "is positive")

"""
prints "odd" or "even" based on number
remember, number % 2 gives 0 when number is disvisible by 2, and 1 otherwise
"""


def printOddOrEven(number):
    if number %2 == 0:
        print(" even")
    elif number %1 == 0:
        print(" odd")


print("6 is", end="")
printOddOrEven(6)
print("7 is", end="")
printOddOrEven(7)
print("8 is", end="")
printOddOrEven(8)
