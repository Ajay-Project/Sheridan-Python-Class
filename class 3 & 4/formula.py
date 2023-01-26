"""
p = float(input("Enter inital investemnt amount:"))
r = float(input("Enter anual intrest rate (as decimal)"))
n = float(input("number of interet compound per year"))
t = float(input("number of years"))

a = p*(1 + r/n)**n**t
print (a)
"""

# Write a program that will compute the area of a circle. 
# Prompt the user to enter the radius and print a nice message back to the user with the answer
"""
r = int(input("enter the radius of the circle"))
area = 3.14 * r * r
print ("The are of the circle is ", area)


#Write a program that will compute the area of a rectangle.
#Prompt the user to enter the width and height of the rectangle.
#Print a nice message with the answer.
"""
"""
l = int(input("Enter the length: "))
w = int(input("Enter thw width: "))
rec_area = l * w
print ("“Every problem has a solution, although it may not be the outcome that was originally hoped for or expected",rec_area)

"""

#Write a program that will compute MPG for a car.
#Prompt the user to enter the number of miles driven and the number of gallons used.
#Print a nice message with the answer.

"""
gallon = int(input("Enter the number of gallon used: "))
miles = int(input("Enter the number of miles driven: "))

MPG = miles / gallon
print ("MPG is :", MPG)


#Write a program that will convert degrees celsius to degrees fahrenheit.

celcius = float(input("Enter the temperature in degress celcius: "))

farh = (celcius * 1.8) + 32
print (farh, "fahrenheit degrees")

"""

#Write a program that will convert degrees fahrenheit to degrees celsius.

fahr = float(input("Enter temp in fahr"))

celcius =