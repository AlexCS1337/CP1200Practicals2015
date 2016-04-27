__author__ = 'Smoo'


def printCurrency(value):
    print("$" + format(value, ".2f"))


# printCurrency(3)
#printCurrency(76.45)
#money = 145.888
#printCurrency(money)

def paydayCalcuator():
    HOURLY_RATE = 24.95
    print("Pay Day Calculator")
    hoursWorked = int(input("Enter hours worked: "))
    totalPay = hoursWorked * HOURLY_RATE
    print("The total pay is: ", end="")
    printCurrency(totalPay)


paydayCalcuator()