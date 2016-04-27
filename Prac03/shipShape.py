__author__ = 'Smoo'

PRICE_OF_SHAPE_A = 5.50
PRICE_OF_SHAPE_B = 12.00
SHIPPING_COST_DISCOUNT = 0.1

def printCurrency(value):
    print("$" + format(value, ".2f"))

shapeA = int(input("How many of shape A: "))
shapeAPrice = 0
if shapeA < 0:
    print("Invalid quantity, using 0")
    ShapeAPrice = 0 * PRICE_OF_SHAPE_A
    printCurrency(shapeAPrice)
else:
    shapeAPrice = shapeA * PRICE_OF_SHAPE_A
    printCurrency(shapeAPrice)

shapeB = int(input("How many of shape B: "))
shapeBPrice = 0
if shapeB < 0:
    print("Invalid quantity, using 0")
    ShapeBPrice = 0 * PRICE_OF_SHAPE_B
    printCurrency(shapeBPrice)
else:
    print("Total cost is: ", end="")
    shapeBPrice = shapeB * PRICE_OF_SHAPE_B
    totalCost = shapeBPrice + shapeAPrice
    if totalCost > 100:
        discountCost = totalCost * SHIPPING_COST_DISCOUNT
        printCurrency(discountCost)
    else:
        printCurrency(totalCost)
