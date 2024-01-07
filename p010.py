from math import sqrt

def  is_prime(n):
    if (n==1 or n ==0):
        return False
    for i in range(2, int(sqrt(n))+1):
        if (n%i == 0):
            return False
    return True

n  = 2000000
s = 2

for i in range(1, n, 2):
    if is_prime(i):
        s += i

print(s)