with open('files/p018.txt', 'r') as triangle:
    tri_list = []
    count = -1
    for line in triangle:
        line = line.split()
        line = [int(i) for i in line]
        tri_list.append(line)
        count += 1

best = 0

for i in range(2**count):
    this = 0
    way = bin(i)[2:]
    if len(way) < count:
        way = '0' * (count - len(way)) + way
    pos = 0 
    for j in range(count+1):
        this += tri_list[j][pos]
        if j < count:
            pos += int(way[j])
    if this > best:
        best = this

print(best)