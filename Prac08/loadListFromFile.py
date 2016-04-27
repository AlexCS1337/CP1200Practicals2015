__author__ = 'Smoo'


def loadListFromFile(filename):
    result = []
    fileIn = open(filename, 'r')
    for line in fileIn:
        result.append(line.rstrip('\n'))
    fileIn.close()
    return result

def loadListFromFile(filename):
    result = []
    fileIn = open(filename, 'r')
    for line in fileIn:
        number = float(line)
        result.append(number)
    fileIn.close()