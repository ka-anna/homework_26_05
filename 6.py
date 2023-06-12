#A number is called a perfect number if it is equal to the sum of
#all of its divisors, not including the number itself. For instance, 6 is a
#perfect number because the divisors of 6 are 1, 2, 3, 6, and 6 = 1 + 2 + 3.
#However,15 is not a perfect number because its divisors
#are 1, 3, 5, 15, and 15 != 1 + 3 + 5. Write
#a program that finds all four of the perfect numbers that are less than 10000.

num=2
sum_d=0

for i in range (num, 10000):
    for j in range (1, i):
        if i % j==0:
            sum_d = sum_d + j
            
    if i == sum_d:
        print(sum_d)
    sum_d=0
