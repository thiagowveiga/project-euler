# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained
# by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


def is_cancellable(a, b):   # checks if the "digit cancellation" can happen on the fraction a/b
    
    a_str = str(a)
    b_str = str(b)
    a_new, b_new = 1, 0


    if a_str[0] in b_str:
        a_new = int(a_str.replace(a_str[0], '', 1))
        b_new = int(b_str.replace(a_str[0], '', 1))
    elif a_str[1] in b_str:
        a_new = int(a_str.replace(a_str[1], '', 1))
        b_new = int(b_str.replace(a_str[1], '', 1))

    if a_new * b == b_new * a:
        return True
    return False

# finding all cases of those fractions
found = []
for i in range(10, 99):
    for j in range(i+1, 100):
        if i%10!=0 and j%10!=0:
            if is_cancellable(i, j):
                found.append([i, j])

# now multiplying all of them and simplifying the result
num, den = 1, 1
for fraction in found:
    num *= fraction[0]
    den *= fraction[1]

def prime_factors(n):
    factors = []
    i = 2
    while n > 1:
        if n%i == 0:
            n = n/i
            factors.append(i)
            i = 2
        i += 1
    return factors

num_factors = prime_factors(num)
den_factors = prime_factors(den)
den_simpl = den_factors[:]
for factor in den_factors:
    if factor in num_factors:
        den_simpl.remove(factor)
        num_factors.remove(factor)

prod_den = 1
for factor in den_simpl:
    prod_den *= factor

print(prod_den)