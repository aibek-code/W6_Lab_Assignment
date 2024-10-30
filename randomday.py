#Aibek Abasov
#10/29/2024
#Problem 2: Select a random day of the week from a list and print: “It was a rainy XXX and the lightning flashed across the sky.”
#The key point was taking a value and storing it in a named variable for later use.

import random

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
selected_day = random.choice(days)
print(f"“It was a rainy {selected_day} and the lightning flashed across the sky.”")

