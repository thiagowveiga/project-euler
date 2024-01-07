import numpy as np
import time

def sum_5p(digits):     # takes either a list with the digits or number

    if type(digits) == int:
        as_list = []
        while digits > 0:
            remain = digits % 10
            digits //= 10
            as_list.insert(0, remain)
    else:
        as_list = digits
    
    as_np = np.array(as_list)
    temp1 = as_np*as_np
    temp2 = temp1*temp1
    as_np_5p = temp2*as_np

    return as_np_5p.sum()

def diff_combs(n_digits):
    start = int(10**(n_digits-1))
    stop = int(10*start)
    diff_combs = []
    for number in range(start, stop):

        digits = []
        while number > 0:
            digits.insert(0, number%10)
            number //= 10
        #digits.insert(0, number)
        
        digits.sort()
        if digits not in diff_combs:
            diff_combs.append(digits)
    diff_combs.sort()
    return diff_combs

def permutate(digits):
    permutations = []

    if len(digits) == 2:
        return digits, [digits[1], digits[0]]

    for d in digits:
        others = digits[:]
        others.remove(d)
        others_perm = permutate(others)
        for perm in others_perm:
            first = [d]
            first.extend(perm)
            if first not in permutations:
                permutations.append(first)
    
    return list(permutations)

def list_to_int(digits):   # returns a list of all possible permutations of the digits as int
    
    permutations = permutate(digits)
    perms_as_int = []
    
    for perm in permutations:
        int_as_str = ''
        for digit in perm:
            int_as_str += str(digit)
        if int_as_str[0] != '0':
            perms_as_int.append(int(int_as_str))

    return perms_as_int

start_time = time.time()

fit_nums = []
for i in range(7):
    candidates = diff_combs(i)
    for number in candidates:
        n_perms = list_to_int(number)
        sum5p = sum_5p(number)
        if sum5p in n_perms and sum5p != 1:
            fit_nums.append(sum5p)

print('')
print(f'sum: {sum(fit_nums)} - {len(fit_nums)} numbers fit the condition')
print(fit_nums)
print(f'\nexecution time: {time.time()-start_time}')