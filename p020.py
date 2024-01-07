from math import factorial

# Find the sum of the digits in the number 100!

k = 100

print(sum([int(i) for i in str(factorial(k))]))