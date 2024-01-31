# Find the sum of the only eleven primes that are both truncatable
# from left to right and right to left.
# (2, 3, 5 and 7 are not considered truncatable primes)

from math import sqrt
import time

def  is_prime(n):
    if (n==1 or n ==0):
        return False
    for i in range(2, int(sqrt(n))+1):
        if (n%i == 0):
            return False
    return True

def is_trunc(num):
    str_num = str(num)
    i = 1
    while i <= len(str_num):
        step = int(str_num[:i])
        if not is_prime(step):
            return False
        step = int(str_num[-i:])
        if not is_prime(step):
            return False
        i += 1
    return True

sum_truncprim = 0
count = 0
start = time.time()
for i in range(13, 1_000_000, 10):
    j = i + 4
    mid_digs = True
    for dig in str(i)[1:-1]:
        if dig not in ['1', '3', '7', '9']:
            mid_digs = False
    if mid_digs and str(i)[0] in ['2', '3', '5', '7']:
        if is_trunc(i):
            print(i)
            sum_truncprim += i
            count += 1
        if is_trunc(j):
            print(j)
            sum_truncprim += j
            count += 1
    if count == 11:
        break
end = time.time()

print(f'sum = {sum_truncprim}')
print(f'time: {round(end-start, 4)}s')