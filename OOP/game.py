#class Student:
#    school = "sheridan" #class vaariable
#    prog = "cloud computing"
#    def __init__(self,name,rollno):
#        self.name = name #instance varibale
#        self.rollno = rollno
#
#    def display(self):
#        print("Name :", self.name , "RollNumber:", self.rollno)
#
#s1 = Student(input("Name"), input("RollNO"))
#s1.display()

class Car:

    def __init__(self,color,price,brand,model):
        self.color = color
        self.price = price
        self.brand = brand
        self.model = model

    def display(self):
        print("color: ",self.color,"price: ",self.price,"brand: ",self.brand,"model: ",self.model)

v1 = Car(input("Color"),input("Price"),input("Brand"),input("Model")) #object variable
v1.display()
v2 = Car(input("Color"),input("Price"),input("Brand"),input("Model"))
v2.display()
v3=Car(input("Color"),input("Price"),input("Brand"),input("Model"))
v1.display()