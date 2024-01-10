import time
from math import log, ceil

def is_palindrome_str(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def is_palindrome_mat(n, base=10):
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

sum_palindromic = 0
for i in range(1, 1_000_000):
    if is_palindrome_str(str(i)) and is_palindrome_str(bin(i)[2:]):
            sum_palindromic += i

end = time.time()

print(f'Sum: {sum_palindromic}')
print('String approach:', f'({round(end-start, 2)}s)')

start = time.time()

sum_palindromic = 0
for i in range(1, 1_000_000):
    if is_palindrome_mat(i, 10) and is_palindrome_mat(i, 2):
            sum_palindromic += i

end = time.time()

print('Mathematical approach: ', f'({round(end-start, 2)}s)')
#print(sum_palindromic)