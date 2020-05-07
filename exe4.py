#TODO: Patter printing
# Input = Integer n
# Boolean = True or False
# True n=4 (n is no. of rows)
# *
# **
# ***
# ****
# .
# False n = 4
# ****
# ***
# **
# *

print("Enter how many line u want to print: ")
n = int(input())
b = bool(input("Type 1 or 0: "))
if b == True:
    for i in range(1, n+1):
        for j in range(1,i+1):
            print('*', end=" ")
        print()
elif b == False:
    for i in range(n, 0, -1):
        for j in range(1,i+1):
            print('*', end=" ")
        print()