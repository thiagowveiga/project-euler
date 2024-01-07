# What is the millionth lexicographic permutation 
# of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# there are 10! permutations of those digits
# they are divided equally with each digit starting 1/10th of them
# each division has 9! permutations and is equally divided with each
# other digit starting 1/9th of them
# and on it goes

from math import factorial

print('\STARTING...\n')
print('type in what digits you want to permutate through')
print('\trepetitions will be discarded')
print('\ttype anything other than a digit to stop ("10", "stop", "sq2mbt7", ...)')

digits = set()

i = input('>> ')
while len(i) == 1 and (ord(i) >= 48) and (ord(i) <= 57):
    digits.add(int(i))
    i = input('>> ')

digits = list(digits)

print('\n')

index = int(input("whats the index of the lexicographic permutation that you want to find?\nfirst = 1, second = 2, etc\n>> "))
print('\n\n')
print(f'CALCULATING the {index}th lexicographic permutation of')
for dig in digits:
    print(f'{dig}', end=' ')
print('\n')

print('...')

divs_size = len(digits) - 1

what_div = index // factorial(divs_size)
new = index % factorial(divs_size)

target = ''

while new != 0:
    target += str(digits.pop(what_div))
    divs_size -= 1
    what_div = new//factorial(divs_size)
    new = new%factorial(divs_size)

target += str(digits.pop(what_div-1))
while digits:
    target += str(digits.pop(-1))

print(f'found! it is\n>> {target}')
print('\nDONE\n')