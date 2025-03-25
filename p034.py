# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# dividing all the integers in sets that go from [10^n] to [10^(n+1) - 1] with n = 0, 1, 2, ...
# the highest fsum (sum of the factorials of the digits of a number) is always the last number in the set (99...)
# as it is only added a 9 to each of those max's, the highest fsum of each set grows linearly by 9! = 362880
# but the value of the number with the highest fsum (99...) grows exponentially
# because of that, after the set that contains 9!, the fsum will always be smaller than its number
# in conclusion it is safe to stablish an upper bound to the search of 999999 (it might be smaller, but this is already enough)

# check <https://colab.research.google.com/drive/15JwcqxZ6p-wFfilQnzC83O6c3O66TusB?usp=sharing#scrollTo=jCLmMQYWERy8> for visualization of that

import time # for performance

def factorial(n):
    
    if n == 0:
        return 1
    
    return n * factorial(n-1)

def sum_fac_dig(n):

    sum_digs = 0

    while n >= 1:
        sum_digs += facts[n%10]
        n //= 10

    return sum_digs

def sum_fac_dig_slow(n):

    sum_digs = 0

    while n >= 1:
        sum_digs += factorial(n%10)
        n //= 10

    return sum_digs

start = time.time()

facts = list(map(factorial, list(range(10))))   # we only use these 10 factorials, so they can be pre calculated

limit = 10000000
sum_ = 0

for i in range(3, limit):
    if sum_fac_dig(i) == i:
        print(i)
        sum_ += i

end = time.time()

print('---\n', sum_)
print(f'time: f{end-start}')

###################################
#   SLOWER METHOD - 5 to 6 slower
###################################

start = time.time()

limit = 10000000
sum_ = 0

for i in range(3, limit):
    if sum_fac_dig_slow(i) == i:
        print(i)
        sum_ += i

end = time.time()

print('---\n', sum_)
print(f'time: f{end-start}')