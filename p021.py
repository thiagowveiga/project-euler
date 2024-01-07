from math import sqrt

def d(n):
    if n == 1:
        return 0
    s = 0
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            s += i
            if n/i < n and n/i != i:
                s += n/i
    return int(s)

under = 10000

number_dn = {n : d(n) for n in range(1, under)}
amicables = []

for i in number_dn:
    j = number_dn[i]
    if j in number_dn and i != j:
        if i == number_dn[j] and i not in amicables and j not in amicables:
            amicables.append(i)
            amicables.append(j)

print(sum(amicables))