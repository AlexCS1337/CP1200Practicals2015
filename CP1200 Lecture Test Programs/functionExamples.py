__author__ = 'Smoo'


from math import sqrt
# import math
# from math import *


def main():
    password = input("Password: ")
    while not isValidPassword(password):
        print("No...")
        password = input("Password: ")


def isValidPassword(password):
    secret = "YeS"
    return password == secret
    # if password == secret:
    # return True
    # else:
    #     return False


# main()


def thingo():
    return 3, sqrt(49)

x, y, z = thingo()

print(type(x))