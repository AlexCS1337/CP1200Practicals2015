__author__ = 'Smoo'


def printCurrency(value):
    print("$" + format(value, ".2f"))

workerLevel = int(input("What is your worker level?: "))
while workerLevel < 1 or workerLevel > 10:
    print("Worker level is too low or too high. Enter again.")
    workerLevel = int(input("What is your worker level?: "))
workerSalary = workerLevel * 5000
print("Your salary is ", end="")
printCurrency(workerSalary)