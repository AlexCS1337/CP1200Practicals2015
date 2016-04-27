__author__ = 'Smoo'


def printLine(width):
    print("-" * width)


def printHello(value):
    print("hello" * value)


def printParity(value):
    print(value % 2)


def printBlank():
    print()


def printReversedWords(x, y):
    print(y, x)


def main():
    printLine(5)
    printBlank()
    printHello(5)
    printParity(5)
    printReversedWords("hello", "mate")


main()

