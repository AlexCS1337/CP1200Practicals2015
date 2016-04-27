__author__ = 'Smoo'


def getValidInteger(prompt,minimum, maximum):
    result = getInteger(prompt)
    while result < minimum or result > maximum:
        print("Please enter an integer between ", minimum, \
              " and ", maximum, ".", sep="")
        result = getInteger(prompt)
    return result