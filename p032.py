# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# each multiplicand/multiplier/product can have the following amount of digits:
#   - 1 x 4 = 4
#   - 2 x 3 = 4

def is_unique(num):     # a unique number is a number that has no repeating digits
    n = str(num)
    if len(n) == len(set(n)):
        return True
    return False

def gen_unique(n):      # generator that yields the unique numbers with n digits
    for i in range(10**(n-1), 10**n):
        if is_unique(i) and '0' not in str(i):
            yield i

def is_pandigital(a, b, c):
    if sorted(str(a)+str(b)+str(c)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    return False

sum_products = 0
found = []

for a in gen_unique(1):     # 1st case
    for b in gen_unique(4):
        c = a*b
        if is_pandigital(a, b, c) and c not in found:
            sum_products += c
            found.append(c)

for a in gen_unique(2):     # 2nd case
    for b in gen_unique(3):
        c = a*b
        if is_pandigital(a, b, c) and c not in found:
            sum_products += c
            found.append(c)

print(sum_products)