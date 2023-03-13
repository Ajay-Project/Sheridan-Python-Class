#Implementation of detail 

class Product():
    def __init__(self, productCode,productName,productSalePrice,prodManuCost,stockLevel,UnitManu):
        self.productCode = productCode
        self.productName =  productName
        self.productSalePrice = productSalePrice
        self.prodManuCost = prodManuCost
        self.stockLevel = stockLevel
        self.UnitManu = UnitManu

    
    def get_product_info():
        productCode = input("Enter Product Code: ")
        productName = input("Enter Product Name: ")
        productSalePrice = input("Enter Product Sale Price: ")
        prodManuCost = input("Enter Product Manfacturing Cost: ")
        stockLevel = input("Enter Stock Level: ")
        UnitManu = input("Enter Estimated Monuthly Manufactured Amount: ")
        return Product(productCode, productName, productSalePrice, prodManuCost, stockLevel, UnitManu)

Product.get_product_info()
