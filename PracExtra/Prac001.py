__author__ = 'Smoo'


# stuff = 25
#
# if stuff == 25:
#     print("Yeah boy")

# hoursWorked = float(input("How many hours are worked?: "))
# hourlyPay = float(input("What is your hourly pay?: "))
# grossPay = hoursWorked * hourlyPay
# print(grossPay)

#Version 1
# temperature = float(input("What is the substance's temperature?: "))
# while temperature > 102.5:
#     print("Turn down the thermostat, wait 5 minutes and check the temperature again.")
#     temperature = float(input("What is the substance's temperature?: "))
# print("The temperature is acceptable. Check again in 15 minutes.")

#Version 2
# MAX_TEMP = 102.5
#
# temperature = float(input("Enter the substance's Celsius temperature: "))
# while temperature > MAX_TEMP:
#     print("The temperature is too high.\n Turn the thermostat down and wait\n 5 minutes. Then take the temperature\n"
#           "again and enter it.")
#     temperature = float(input("Enter the substance's Celsius temperature: "))
#
# print("The temperature is acceptable.")
# print("Check it again in 15 minutes.")

fileOut = open("text.txt", "r")
fileOut.close()

fileIn = open("text.txt", "w")
fileIn.close()

