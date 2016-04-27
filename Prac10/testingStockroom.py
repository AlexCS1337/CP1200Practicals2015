__author__ = 'Smoo'


import stockroom

stockRoom = stockroom.StockRoom()
stockRoom.addProduct("pen", 20)
stockRoom.addProduct("pencil", 50)
stockRoom.addProduct("ruler", 5)
stockRoom.withdrawProduct("pen", 1)
stockRoom.withdrawProduct("ruler", 10)

products = stockRoom.getAllStockedProducts()
products.sort()
for product in products:
    print(product, ": ", stockRoom.getProductQuantity(product), sep="")
