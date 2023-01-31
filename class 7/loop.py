#def sumTo(aBound):
#    theSum = 0
#    for aNumber in range(1, aBound + 1):
#        theSum = theSum + 1/(aNumber ** aNumber)
#
#    return theSum
#
#print(sumTo(6))


def factorial(number):
    theNumber=1
    for number in range(1,number +1):
        theNumber = theNumber * number
    return theNumber
    
number = int(input("ENTER A NUMBER: "))
print(factorial(number))