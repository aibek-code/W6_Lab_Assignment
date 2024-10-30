#Aibek Abasov
#10/29/2024
#Problem 4: Calculate the factorial of a user-input value using both the factorial function from the math module and a for loop. Print the comparison of the two results.
#For me factorial function was new in this assignment.

import math


num = int(input("Enter a non-negative integer to calculate its factorial: "))

factorial_math = math.factorial(num)

factorial_loop = 1
for i in range(1, num + 1):
    factorial_loop *= i

print(f"Factorial using math.factorial: {factorial_math}")
print(f"Factorial using for loop: {factorial_loop}")

if factorial_math == factorial_loop:
    print("Both methods give the same result.")
else:
    print("The results differ.")