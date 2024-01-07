# Find the value of d < 1000 for which 1/d contains 
# the longest recurring cycle in its decimal fraction part.

# usar que na "divisao de pe" sabe que ficou recorrente se encontra um
# resto ja encontrado no processo!

def n_recurring(d):
    if d == 0:
        return 0
    rem = 1
    already = [1]    # list of remainders that have already appeared
    while True:
        rem = (10*rem)%d
        if rem == 0:
            return 0
        elif rem in already:
            return (len(already) - already.index(rem))
        already.append(rem)

upto = 1000
longest = (0, 1)

for i in range(upto):
    k = n_recurring(i)
    if k > longest[0]:
        longest = (k, i)

print(f'The longest recurring cycle is for 1/{longest[1]}\n(period {longest[0]})')