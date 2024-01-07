with open('files/p018.txt', 'r') as triangle:
    tri_list = []
    count = 0
    for line in triangle:
        line = line.split()
        line = [int(i) for i in line]
        tri_list.append(line)
        count += 1

for i in range(count-2, -1, -1):
    for j in range(len(tri_list[i])):
        tri_list[i][j] += max(tri_list[i+1][j], tri_list[i+1][j+1])

print(tri_list[0][0])