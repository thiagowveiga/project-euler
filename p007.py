from math import sqrt

def  is_prime(n):
    if (n==1 or n ==0):
        return False
    for i in range(2, int(sqrt(n))+1):
        if (n%i == 0):
            return False
    return True


k = 10001
count = 0
i = 0
while count < k:
    if is_prime(i):
        count += 1
    i += 1

print(i-1)