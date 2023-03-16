#Implementation of detail 
import random

class Product:
    def __init__(self, productCode,productName,productSalePrice,prodManuCost,stockLevel,UnitManu):
        self.productCode = productCode
        self.productName =  productName
        self.productSalePrice = productSalePrice
        self.prodManuCost = prodManuCost
        self.stockLevel = stockLevel
        self.UnitManu = UnitManu #monthy

    
    def get_product_info(self):
        productCode = int(input("Enter Product Code: "))
        productName = input("Enter Product Name: ")
        productSalePrice = float(input("Enter Product Sale Price: "))
        prodManuCost = float(input("Enter Product Manfacturing Cost: "))
        stockLevel = int(input("Enter Stock Level: "))
        UnitManu = int(input("Enter Estimated Monthly Manufactured Amount: "))
        
    def __str__(self):
        return f"Product Code: {self.productCode}\nProduct Name: {self.productName}\nSale Price: ${self.productSalePrice}\nManufacture Cost: ${self.prodManuCost}\nMonthly Production: {self.UnitManu}\n"


    def simulate_monthly(self,predictStock):
        #SALE OF PRODUCT
        unitSold = random.randint(self.UnitManu - 10 or self.UnitManu + 10)
        sale_of_product = unitSold
        predictStock = self.UnitManu - self.unitSold
        return (sale_of_product,predictStock)

    
    def stock_prediction(self):
        for i in range(1,13):
















