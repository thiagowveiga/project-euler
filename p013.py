s = 0
with open('files/p013.txt') as numbs:
    for num in numbs:
        s += int(num)
print(s)
s = str(s)
print(f'\no numero acima tem {len(s)} digitos! ay caramba')