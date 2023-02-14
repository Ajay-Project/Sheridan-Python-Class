"""
a = ["banana", "apple","Mircosoft"]
#print(a[0])
#print(a[1])
#print(a[2])

for element in a:
    print(element)
    print(element)


b = [20,10,5]
total = 0
for element in b:
    total = total + element
print(total)

number = list(range(1,5))
print(number)

total = 0
for i in list(range(1,5)):
    total = total + i
print(total)

print(list(range(1,8)))
total = 0
for i in range(1,8):
    if i % 3 == 0:
        total += i
print(total)
"""
total = 0
for i in range(1,100):
    if i % 3 ==0 or i % 5 == 0:
        total += i
print(total)