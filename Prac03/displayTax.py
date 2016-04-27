__author__ = 'Smoo'


def printCurrency(value):
    print("$" + format(value, ".2f"))


TAX_RATE_LOW = 0.05  # 5%
TAX_RATE_HIGH = 0.1  # 10%
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_HIGH = 1000

print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))
if income < TAX_THRESHOLD_LOW:
    taxAmount = 0
elif income >= TAX_THRESHOLD_LOW:
    taxAmount = income * TAX_RATE_LOW
elif income > TAX_THRESHOLD_HIGH:
    taxAmount = income * TAX_RATE_HIGH
takeHomePay = income - taxAmount
print("Total tax is: ", end="")
printCurrency(taxAmount)
print("Take home pay is: ", end="")
printCurrency(takeHomePay)