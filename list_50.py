#Write a program that
#generates and prints 50 random integers, each between 3 and 6.

import random
my_list = [3,4,5,6]
print (random.choices(my_list, k = 50))
