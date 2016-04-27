"""
Pythonville Hospital Medical Records Manager

Created: 05/04/2013 by Trevor Andersen
"""
CHECK_OPTION = "1"
CREATE_OPTION = "2"
VIEW_OPTION = "3"
ADD_OPTION = "4"
QUIT_OPTION = "5"
PATIENTS_FILE = "patients.txt"

def main():
    print('Pythonville Hospital Medical Records Manager')
    print()
    
    displayMenu()
    option = input("Enter your choice: ")

    while option != QUIT_OPTION:
        if option == CHECK_OPTION:
            checkIfPatientInSystem()
        elif option == CREATE_OPTION:
            createNewRecord()
        elif option == VIEW_OPTION:
            viewRecord()
        elif option == ADD_OPTION:
            addRecord()
        else:
            print("Please enter a valid option.")

        displayMenu()
        option = input("Enter your choice: ")        

def displayMenu():
    print("1. Check if a patient is in the system")
    print("2. Add a new patient to the system")
    print("3. View medical record")
    print("4. Add to medical record")
    print("5. Quit")    

def checkIfPatientInSystem():
    print("checkIfPatientInSystem")

def createNewRecord():
    print("createNewRecord")

def viewRecord():
    print("viewRecord")

def addRecord():
    print("viewRecord")

main()
