""" Once Again Another 1st Prac Script
Alex Silva, 02/03/2015
"""
landCost = float(input("What is the land cost?: "))
houseSize = float(input("What is the house size in m2?: "))
pricePerM2 = float(input("What is the price per m2?: "))
houseCost = houseSize * pricePerM2
totalCost = houseCost + landCost
print("The total house & land package price is", totalCost)
