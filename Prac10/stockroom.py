

class StockRoom:
    def __init__(self):
        self._productQuantityDict = {}

    def getProductQuantity(self, productName):
        if productName in self._productQuantityDict:
            return self._productQuantityDict[productName]
        else:
            return 0 
    
    def withdrawProduct(self, productName, quantity):
        if productName not in self._productQuantityDict:
            return 0
        if quantity > self._productQuantityDict[productName]:
            withdrawnQuantity = self._productQuantityDict[productName]
            self._productQuantityDict[productName] = 0
            return withdrawnQuantity
        else:
            self._productQuantityDict[productName] -= quantity
            return quantity
        
    def addProduct(self, productName, quantity):
        if productName in self._productQuantityDict:
            self._productQuantityDict[productName] += quantity
        else: 
            self._productQuantityDict[productName] = quantity
            
    def getAllStockedProducts(self):
        stockedProducts = []
        for product in self._productQuantityDict:
            if self._productQuantityDict[product] > 0:
                stockedProducts.append(product)
        return stockedProducts
        