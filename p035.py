# How many circular primes are there below one million?

from math import sqrt
import time

def  is_prime(n):
    if (n==1 or n ==0):
        return False
    for i in range(2, int(sqrt(n))+1):
        if (n%i == 0):
            return False
    return True

def gen_rotations(n):
    n = str(n)
    rotations = []
    for i in range(len(n)):
        if n[i] != '0':
            curr = n[i]
            j = i + 1
            while j != i and len(curr) < len(n):
                if j == len(n):
                    j = 0
                curr += n[j]
                j += 1
            if int(curr) not in rotations:
                yield int(curr)
                rotations.append(int(curr))

def is_circular_prime(n):
    circular_prime = True
    rots = gen_rotations(n)
    for rotation in rots:
        if not is_prime(rotation):
            return False
    return True

count = 13
step = list(range(-1, 1_000_000, 100_000))
print('\nstarting...')
start = time.time()
last = start
for i in range(100, 1_000_000):
    if is_circular_prime(i):
        count += 1
    if i in step:
        if i == step[-1]:
            print(f'{int((i+1)/1_000_000*100)}% ({round(time.time()-last, 2)}s)', flush=True)
        else:
            print(f'{int((i+1)/1_000_000*100)}% ({round(time.time()-last, 2)}s) ...', flush=True, end=' ')
        last = time.time()
print(f'DONE! ({round(time.time()-start, 2)}s)')

print('')
print(f'There are {count} circular primes below one million!\n')