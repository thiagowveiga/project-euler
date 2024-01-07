# A perfect number is a number for which the sum of its proper divisors
# is exactly equal to the number. For example, the sum of the proper 
# divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28

# A number n is called deficient if the sum of its proper divisors 
# is less than n and it is called abundant if this sum exceeds n.

# Find the sum of all the positive integers which cannot be written 
# as the sum of two abundant numbers.

# --

# the double of an abundant number is also abundant

from math import sqrt

def is_abundant(n):
    if n==0:
        return False
    proper_divisors = [1]
    for i in range(2, int(sqrt(n))+1):
        if (n%i == 0):
            proper_divisors.append(i)
            if i != sqrt(n):
                j = n // i
                proper_divisors.append(j)
    if sum(proper_divisors) > n:
        return True
    else:
        return False

limit = 28123
abundants = []

for i in range(limit):
    if (is_abundant(i)):
            abundants.append(i)

n_as_2_abund = set()

for i in abundants:
    for j in abundants:
        if (i+j) <= limit:
            n_as_2_abund.add(i+j)

print(sum(range(limit+1)) - sum(n_as_2_abund))