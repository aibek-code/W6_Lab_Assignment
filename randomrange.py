#Aibek Abasov
#10/29/2024
#Problem 1: Use a for loop and randrange to generate and print 10 random integers between 25 and 35, storing them in a list called rand_nums.
#Inside the loop, random.randrange( ) generates a random integer

import random

rand_nums = []

for _ in range(10):
    num = random.randrange(25, 36)  
    rand_nums.append(num)            
    print(num)                       

print("Random Numbers List:", rand_nums)