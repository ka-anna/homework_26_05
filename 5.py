#A year is a leap 20year if it is divisible by 4, except that years
#divisible by 100 are not leap years unless they are also divisible by 400.
#Ask the user to enter a year, and, using the // operator,
#determine how many leap years there have been between 1600 and that year.

inp_y = int(input("enter a year "))
leap_y = 0
for i in range(inp_y, 1600):
    if (i/400-i//400)==0:
        leap_y = leap_y+1
    elif i/100-i//100==0:
        leap_y = leap_y
    elif i/4-i//4 == 0:
        leap_y = leap_y+1
print(leap_y)



