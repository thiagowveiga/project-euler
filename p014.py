def count_chain(n):
    if n in values:
        return values[n]
    
    if n%2 == 0:
        values[n] = count_chain(int(n/2)) + 1
    else:
        values[n] = count_chain(int((3*n+1)/2)) + 2
    
    return values[n]

upto = 1000000

max_length = 0
max_initial = 1

values = {1:1}

for i in range(int(upto/2), upto):
    k = count_chain(i)
    if k > max_length:
        max_length = k
        max_initial = i

print(max_initial)