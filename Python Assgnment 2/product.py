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
        
   #def __str__(self):
    #   return f"Product Code: {self.productCode}\nProduct Name: {self.productName}\nSale Price: ${self.productSalePrice}\nManufacture Cost: ${self.prodManuCost}\nMonthly Production: {self.UnitManu}\n"


    def simulate_monthly(self):
        #SALE OF PRODUCT
        unitSold = random.randint(self.UnitManu - 10,self.UnitManu + 10)
        sale_of_product = unitSold
        predictStock = self.UnitManu - sale_of_product
        return (sale_of_product,predictStock)

    
    def stock_prediction(self):
        for i in range(1,13):
            maunfactured_unit = self.UnitManu + random.randint(0,200)
            unit_sold = random.randint(0, maunfactured_unit)
            stock_remain = maunfactured_unit - unit_sold
            net_profit = (unit_sold * self.productSalePrice) - (maunfactured_unit * self.prodManuCost)
            return (maunfactured_unit,unit_sold,stock_remain,net_profit)

            















