#import matplotlib.pyplot as plt
#import numpy as np
#
#plt.style.use('_mpl-gallery')
#
## make data
#x = np.linspace(0, 10, 100)
#y = 4 + 2 * np.sin(2 * x)
#
## plot
#fig, ax = plt.subplots()
#
#ax.plot(x, y, linewidth=2.0)
#
#ax.set(xlim=(0, 8), xticks=np.arange(1, 90),
#       ylim=(0, 8), yticks=np.arange(1, 8))
#
#plt.show()

# s = "if():,print():"
# for eachChar in s :
#     print(eachChar)

#ef removeLet(s):
#   letter = "():,"
#   sRoverLeetter = ""
#   for eachChar in s:
#       if eachChar not in letter:
#           sRoverLeetter = sRoverLeetter + eachChar
#   return sRoverLeetter
#
#rint(removeLet("sajy:()"))

def passwordchecker(s):
    sym = "@#&$"
    flag=False
    for eachChar in s:
        if eachChar in sym:
            flag=True
            break
    if flag:
        print ("Vaalid Password")
    else:
        print("Invalid Password")

print(passwordchecker("ajaypersaud4@gmail.com"))