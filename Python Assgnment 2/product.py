#Implementation of detail 
import random

class Product:
    def __init__(self):
        self.productCode = int(input("Enter Product Code: "))
        self.productName = input("Enter Product Name: ")
        self.productSalePrice = float(input("Enter Product Price: "))
        self.prodManuCost = float(input("Enter Product Manfacturing Cost: "))
        self.UnitManu = int(input("Enter Estimated Monthly Manufactured Amount: "))
        self.monthlySales = []

    def simulate_monthly_sale(self):
        for i in range(12):
            unitSold = random.randint(self.UnitManu - 10, self.UnitManu + 10)
            self.monthlySales.append(unitSold)


    def display_prediction_stock_statement(self):
        print("Product Code: ", self.productName)
        print("Product Name: ",self.productName)
        print("Sale Price: ", self.productSalePrice)
        print("Manufacture Cost: ", self.prodManuCost)
        print("Monthy Production : ",self.UnitManu, "Apx")
        print("Predicted Monthly Stock for Next 12 Months:")
        soldProduct = 0
        totalUnitManu = 0
        for m in range(13):
            monthlyStock = self.UnitManu - self.monthlySales[m]
            soldProduct += self.monthlySales[m]
            totalUnitManu += self.UnitManu
            print((f"Month{m-1}: Monthly Stock {monthlyStock}"))
        netProfit = (soldProduct * self.productSalePrice) - (totalUnitManu * self.prodManuCost)
        print("NET PROFIT/LOSE",(netProfit))


  
b = Product()
b.simulate_monthly_sale()
b.display_prediction_stock_statement()









