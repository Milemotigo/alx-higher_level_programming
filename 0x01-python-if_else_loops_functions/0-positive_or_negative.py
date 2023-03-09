#!/usr/bin/python3
import random
# Generate a random number between -10 and 10 inclusive
number = random.randint(-10, 10)
# Check if the number is positive
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
# check if the above statement is not satisfied which means the number is negative
else:
    print(f"{number} is negative")
