#class A:
#    def ima(self):
#        print("im A")
#
#class B(A):
#    def __init__(self):
#        print("I am Class B")
#
#    def imb(self):
#        print("Im class B")
#
#
#ob = A()
#obb = B()
#obb.ima() 
#obb.imb()

#print(isinstance(obb, A)) #True because of INHERTANCE
#print(isinstance(ob, B)) #False

#CHILD Class can access PARENT class but parent cant accesss CHILD class

class Employee:
    def __init__(self):
        pass

class Salary(Employee):
    def calcualtor_Pay_roll(self):
        pass

class HourlyEmployee(Employee):
    def calcualtor_Pay_roll(self):
        pass

class ComissionEmpl(Salary):
    def calcualtor_Pay_roll(self):
        pass