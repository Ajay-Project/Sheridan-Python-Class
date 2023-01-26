#get 2 value from user and check if the first value is a multiple of the second

value1 = int(input("Enter a number:  "))
value2 = int(input("Enter a number:  "))

if value1 % value2 == 0:
    print("Yes {} is a multiple of {}".format(value1,value2))
else:
    print("NO {} is not a multiple of {}".format(value1,value2))