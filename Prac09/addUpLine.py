__author__ = 'Smoo'


def main():
    filename = input("Enter the filename: ")
    fileIn = open(filename, 'r')
    i = 1
    for line in fileIn:
        total = addUpLine(line)
        print("Total for line ", i, "is ", total, ".", sep="")
    fileIn.close()

def addUpLine(line):
    parts = line.split()
    total = 0
    for number in parts:
        total += int(number)
    return total

main()