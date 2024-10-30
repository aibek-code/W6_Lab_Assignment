#Aibek Abasov
#10/29/2024
#Problem 3: Flip a coin 1000 times, where it lands on "heads" X% of the time and "tails" (100-X)% of the time. Keep track of the results and find out the percentage of flips that were "heads."
#random.random() function which generates a random floating-point number between 0.0 and 1.0 was the hardest part for me.

import random

X = 21  
num_flips = 1000

results = []

for _ in range(num_flips):
    if random.random() < X / 100:  
        results.append("heads")
    else:
        results.append("tails")

heads_count = results.count("heads")
heads_percentage = (heads_count / num_flips) * 100

print(f"Number of heads: {heads_count}")
print(f"Percentage of heads: {heads_percentage:.2f}%")

