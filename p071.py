# 2/5 = 0.4
# 3/7 = 0.42857

from math import sqrt

def  is_prime(n):
    if (n==1 or n ==0):
        return False
    for i in range(2, int(sqrt(n))+1):
        if (n%i == 0):
            return False
    return True

def prime_range(n):
    primes = []
    for i in range(n):
        if is_prime(i):
            primes.append(i)
    return primes

upto = 1000000
primes = prime_range(upto)

def reduce_to_proper(n, d):
    a = n
    b = d
    proper = True
    for i in primes:
        if i >= d:
            break
        while not a%i and not b%i:
            a /= i
            b /= i
            proper = False
    return int(a), int(b), proper

max = 2/5
num = 2
den = 5    

for i in range(1, upto):
    if  i%7:
        sup = int(3*i/7)
    else:
        sup = int(3*i/7 - 1)
    k = sup/i
    if k > max:
        max = k
        num = sup
        den = i

print(f'{int(num)}/{int(den)}')