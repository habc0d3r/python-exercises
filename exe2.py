#Todo:Exercise2 :: Faulty calculator
# Design a calculator which will correctly solves all the problems
# except the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# and pr0gram should take operator and the two
# numbers from the user as input and then return the result

print("1st number: ")
fn = int(input())
print("2nd number: ")
sn = int(input())
print("Enter your operator: ")
op = input()

if fn == 45 and sn == 3 and op == '*':
    print(int(555))
elif fn == 56 and sn == 9 and op =='+':
    print(int(77))
elif fn == 56 and sn == 6 and op =='/':
    print(int(4))
elif op == '*':
    a = fn*sn
    print(a)
elif op =='+':
    b = fn+sn
    print(b)
elif op == '/':
    c = fn/sn
    print(c)
else:
    print("error! Please check your input.")