from math import log, ceil
import time

def reverse(n, base=10):
    k = n
    rev = 0
    while k > 0:
        rev = rev*base + k%base
        k //= base
    return rev

def gen_palindrome(limit, base=10):
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
        while root< next_order:
            pld = root*(base**(l+1)) + reverse(root, base)%(base**(l+1))
            if pld >= limit: break
            yield pld
            root += 1

###### performance measurements ######

def sort_by_index(ll, i, order='desc'):
    if order == 'asc':
        for m in range(len(ll)-1):
            for n in range(m+1, len(ll)):
                if ll[n][i] < ll[m][i]:
                    ll[m], ll[n] = ll[n], ll[m]
    else:
        for m in range(len(ll)-1):
            for n in range(m+1, len(ll)):
                if ll[n][i] > ll[m][i]:
                    ll[m], ll[n] = ll[n], ll[m]
    return ll

limit = 100_000_000

b_times_sums = []

for base in range(2, 17):
    start = time.time()
    s = 0
    count = 0
    for i in gen_palindrome(limit, base):
        s += i
        count += 1
    end = time.time()
    b_times_sums.append((base, end-start, s, count))


print('#'*70)
print('#'+' '*24+'ORDERED BY LESS TIME'+' '*24+'#')
print('#'*70)
for i, b in enumerate(sort_by_index(b_times_sums, 1, order='asc')):
    s = ' '*70
    s = f'{i+1})' + s[1:]
    s = s[:4] + f'BASE {b[0]}   ' + s[5:]
    s = s[:14] + f'TIME: {round(b[1], 4)}s   ' + s[15:]
    s = s[:30] + f'SUM: {b[2]}' + s[31:]
    s = s[:52] + f'COUNT: {b[3]}' + s[53:]
    print(s)

print('#'*70)
print('#'+' '*24+'ORDERED BY LESS SUM'+' '*25+'#')
print('#'*70)
for i, b in enumerate(sort_by_index(b_times_sums, 2, order='asc')):
    s = ' '*70
    s = f'{i+1})' + s[1:]
    s = s[:4] + f'BASE {b[0]}   ' + s[5:]
    s = s[:14] + f'TIME: {round(b[1], 4)}s   ' + s[15:]
    s = s[:30] + f'SUM: {b[2]}' + s[31:]
    s = s[:52] + f'COUNT: {b[3]}' + s[53:]
    print(s)

print('#'*70)
print('#'+' '*24+'ORDERED BY LESS COUNT'+' '*23+'#')
print('#'*70)
for i, b in enumerate(sort_by_index(b_times_sums, 3, order='asc')):
    s = ' '*70
    s = f'{i+1})' + s[1:]
    s = s[:4] + f'BASE {b[0]}   ' + s[5:]
    s = s[:14] + f'TIME: {round(b[1], 4)}s   ' + s[15:]
    s = s[:30] + f'SUM: {b[2]}' + s[31:]
    s = s[:52] + f'COUNT: {b[3]}' + s[53:]
    print(s)