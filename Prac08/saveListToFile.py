__author__ = 'Smoo'


def saveListToFile(filename, data):
    fileOut = open(filename,'w')
    for datum in data:
        fileOut.write(datum + '\n')
    fileOut.close()