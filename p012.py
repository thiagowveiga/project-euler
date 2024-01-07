from math import sqrt

def get_num(n):
    soma = 0
    for i in range(1, n+1):
        soma += i
    return soma

def how_many_divisors(n):
    count = 0
    i = 1
    limit = sqrt(n)
    while i < limit:
        if n%i == 0:
            count += 1
        i += 1
    count *= 2
    if i == limit:
        count += 1
    return count

num = 0
i = 1

while num <= 500:
    k = get_num(i)
    num = how_many_divisors(k)
    i += 1

print(k)