#Write a program that asks the user to
#enter two numbers, x, and y, and computes | x − y | /  x+y.
x = float(input("enter x="))
y = float(input("enter y="))
exp1 = x-y
if exp1 <0:
    exp1 = exp1 * (-1)
exp2 = x+y
if exp2 >0:
    result = exp1/exp2
    print(result)
else:
    print("Error")

