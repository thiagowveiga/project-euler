# considering quadratics of the form
#   n² + an + b where |a| < 1000 and |b| <= 1000
# 
# find the product of the coefficients a and b so that it makes
# the maximum # of primes for consecutive n's

# note that b always has to be prime, because the expression = b, 
# when n = 0

# a² - 4b < 0 -> a² < 4b -> |a| < 2.sqrt(b)



from math import sqrt, ceil

def is_prime(n):
    if n <= 0:
        return False
    limit = ceil(sqrt(n)) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True

def prime_upto(a, b):
    prime = True
    i = 0
    while prime == True:
        exp = i**2 + a*i + b
        prime = is_prime(exp)
        i += 1
    return i-2

primes_u1000 = []
for i in range(1001):
    if is_prime(i):
        primes_u1000.append(i)

max_nprimes = 0
prod_max = 0

for b in primes_u1000:
    a_limit = ceil(2 * sqrt(b))
    a = -1 * a_limit + 1
    while a < a_limit:
        k = prime_upto(a, b)
        if k > max_nprimes:
            max_nprimes = k
            prod_max = a*b
        a += 1

print(prod_max)