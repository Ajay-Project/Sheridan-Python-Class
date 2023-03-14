#Implementation of detail 
import random

class Product():
    def __init__(self, productCode,productName,productSalePrice,prodManuCost,stockLevel,UnitManu):
        self.productCode = productCode
        self.productName =  productName
        self.productSalePrice = productSalePrice
        self.prodManuCost = prodManuCost
        self.stockLevel = stockLevel
        self.UnitManu = UnitManu

    
    def get_product_info():
        productCode = int(input("Enter Product Code: "))
        productName = input("Enter Product Name: ")
        productSalePrice = float(input("Enter Product Sale Price: "))
        prodManuCost = float(input("Enter Product Manfacturing Cost: "))
        stockLevel = int(input("Enter Stock Level: "))
        UnitManu = int(input("Enter Estimated Monuthly Manufactured Amount: "))
        return Product(productCode, productName, productSalePrice, prodManuCost, stockLevel, UnitManu)  

    def simulate_monthly():
        unitSold = randon.randint(self.UnitManu - 10 or self.UnitManu + 10)
        return unitSold
        
        
    def stock_prediction():
        pass
       
















