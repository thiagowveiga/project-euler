with open('files/p022.txt', 'r') as fnames:
    names = fnames.read().replace('"', '').split(',')
    names.sort()

total_score = 0

for i in range(len(names)):
    name_score = 0
    for j in names[i]:
        name_score += (ord(j)-64)
    total_score += (i+1)*name_score

print(total_score)