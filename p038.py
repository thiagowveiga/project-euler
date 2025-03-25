import time

def permutations(s):    # returns all permutations of a iterable (doesnt account for repetitions)
    n = len(s)
    if n == 1:
        yield [s]
    for i in range(n):
        a = s[i]
        rem = s[:i]+s[i+1:]
        for perm in permutations(rem):
            yield [a] + perm

def is_concprod(num):

# note: the numbers in () in this comment section are the number of digits of each calculated product of the starting integer to be concatenated
#   the numbers in () must add up to 9
#   the next product to be concatenated must have the same number of digits as the one before or one more
# a concatenated product can't be obtained from an integer with 5 or more digits
# it can be obtained from an integer with 4 digits (4+5=9) -> the starting integer must be greater than 6000
# it can be obtained from an integer with 3 digits (3+3+3=9) -> the starting integer must be less than 333
# it can't be obtained from an integer with 2 digits
#   the only possible integers for (2+2+2+3=9) are 31 and 32 and neither of them work
#   for (2+3+4=9) to work there would need to be a 2 digit number that times 3 was a 4 digit number, which is obviously impossible
# it can be obtained from an integer with 1 digit.

    if int(num[:4])*2 == int(num[4:]):
        return True
    if int(num[:3])*2 == int(num[3:6]) and int(num[:3])*3 == int(num[6:9]):
        return True
    start = int(num[0])
    nex = 2*start
    rem = num[1:]
    while rem.startswith(str(nex)):
        nex += start
        rem = rem[len(str(nex)):]
        if not rem:
            return True
    return False

t0 = time.time()

for p in permutations('987654321'):
    if is_concprod(''.join(p)):
        print(''.join(p))
        break

tf = time.time()

print(f'runtime: {tf-t0:.6f}s')