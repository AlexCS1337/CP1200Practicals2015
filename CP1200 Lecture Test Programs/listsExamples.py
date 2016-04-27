__author__ = 'Smoo'


def formatString2(things, seperator):
    string = ""

    for thing in things[:-1]:
        string += str(thing) + seperator
    string += str(things[-1])
    return string


def formatString(things, seperator):
    string = ""

    for thing in things:
        string += str(thing) + seperator
    return string[:-len(seperator)]

print(formatString([1, 2, 3], '---'))
print(formatString2([1, 2, 3], '---'))
print(formatString([], ''))


# name = input("Name: ")
# while True:
#     choice = input("Char: ")
#     while len(choice) != 1 or choice == "":
#         print("Type in only one character please.")
#         choice = input("Chat: ")
#
#
#     if choice in list(name):
#         print("Yes that's in your name")
#     else:
#         print("No. ")