# display the menu and return the choice
def getMenuChoice():
    print("Menu:")
    print("w. write a new file")
    print("r. read a file and display to the screen")
    print("q. quit")
    choice = input("Enter your choice: ")

    return choice

def getNonEmptyString(prompt, errorMessage):
    string = input(prompt)
    while string == "":
        string = input(prompt)
        print(errorMessage)
        
    return string

# get the user to enter y or n
# return True if y, False if n
# Note the valid use of while True here - since the loop exits when the function returns
def getConfirmation(prompt, errorMessage):
    string = input(prompt).lower()
    while True:
        if string == 'y':
            return True;
        elif string == 'n':
            return False
        else:
            print(errorMessage)
        string = input(prompt).lower()

def writeNewFile():
    filename = getNonEmptyString("Enter the filename: ", \
                                 "Filename cannot be blank!")
    fileOut = open(filename, 'w')

    keepGoing = True
    lineCount = 0
    while keepGoing:
        lineCount += 1
        line = input("Enter line" + str(lineCount) + ": ")
        fileOut.write(line + '\n')
        
        keepGoing = getConfirmation("Enter another line (y/n)?", \
                                    "Please enter y or n.")

    print("Wrote", lineCount, "lines to", filename)    
    fileOut.close

def readAndDisplayFile():
    filename = getNonEmptyString("Enter the filename: ", \
                                 "Filename cannot be blank!")

    fileIn = open(filename, "r")
    text = fileIn.read()
    fileIn.close()

    print("Displaying ", filename, "...", sep="")
    print(text)

def main():
    print("VSFRW")
    print()

    choice = getMenuChoice()
    while choice != 'q':
        if choice == 'w':
            writeNewFile()
        elif choice == 'r':
            readAndDisplayFile()
        else:
            print("Invalid choice!")
        choice = getMenuChoice()

    print()
    print("Adios.")
            

main()
