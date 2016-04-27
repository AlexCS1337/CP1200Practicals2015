__author__ = 'Smoo'


filename = input("Enter the name of the file (enter nothing to quit): ")
while filename != "":
    fileIn = open(filename, 'r')
    count = 1
    line = fileIn.readline().strip()
    while line != "":
        print("Line", str(count) + ":", line)
        line = fileIn.readline().strip()
        if line != "":
            count != 1
            input("Please enter to see line " + str(count) + "....")
        else:
            input("You have reached the end of the file. Press enter to finish.")

    filename = input("Enter the name of the file (enter nothing to quit: ")

