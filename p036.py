# Find the sum of all
# numbers less than one million, which are palindromic in base 10 and base 2.

# the "mathematical approach" is heavily based on the overview avaiable
# on <https://projecteuler.net/overview=0036>"

import time
from math import log, ceil

limit = 1_000_000_000_000

def reverse(n, base=10):
    k = n
    rev = 0
    while k > 0:
        rev = rev*base + k%base
        k //= base
    return rev

def gen_palindrome(limit, base=10):     # also from the overlook - gets the code more than 30x faster
    root = 1
    pld = 0
    while pld < limit:
        root_save = root
        next_order = base*root_save
        l = ceil(log(root, base))
        while root < next_order:
            pld = root*(base**(l)) + reverse(root, base)%(base**(l))
            if pld >= limit: break
            yield pld
            root += 1
        root = root_save
        if pld >= limit: break
        while root < next_order:
            pld = root*(base**(l+1)) + reverse(root, base)%(base**(l+1))
            if pld >= limit: break
            yield pld
            root += 1

def is_palindrome_str(s):   # string approach (faster)
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def is_palindrome_mat(n, base=10):  # math approach
    if n == 1:
        return True
    k = n
    rev = 0
    i = 1
    while k > 0:
        rev = rev*base + k%base
        k //= base
        if rev != n//(base**(ceil(log(n, base)) - i)):
            return False
        i += 1
    return True

start = time.time()
base = 10
sum_palindromic = 0
highest = 0
for i in gen_palindrome(limit, base):
    if is_palindrome_str(str(i)) and is_palindrome_str(bin(i)[2:]):
        if i > highest: highest = i
        sum_palindromic += i

end = time.time()

print(f'Search limit: {limit:,}')
print(f'Highest palindrome found: {highest:,}[10] - {bin(highest)[2:]}[2]')
print(f'Sum: {sum_palindromic:,}')
print('BASE 10:', f'({end-start:.6f}s)')

start = time.time()
base = 2
sum_palindromic = 0
for i in gen_palindrome(limit, base):
    if is_palindrome_str(str(i)) and is_palindrome_str(bin(i)[2:]):
        sum_palindromic += i

end = time.time()
print('BASE 2: ', f'({end-start:.6f}s)')

# start = time.time()

# sum_palindromic = 0
# for i in gen_palindrome(limit, 10):
#     if is_palindrome_mat(i, 10) and is_palindrome_mat(i, 2):
#             sum_palindromic += i

# end = time.time()

# print('Mathematical approach: ', f'({round(end-start, 4)}s)')
# #print(sum_palindromic)