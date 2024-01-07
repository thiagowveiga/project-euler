import numpy as np
from termcolor import cprint

grid = []
with open('files/p011.txt') as txt:
    for line in txt:
        lin = line.split()
        for i in range(0, len(lin)):
            lin[i] = int(lin[i])
        grid.append(lin)
        
grid = np.array(grid)
t_grid = grid.transpose()

pos1 = [0, 0]
pos2 = [0, 0]
pos3 = [0, 0]
pos4 = [0, 0]

product = (-1) * np.inf
n = 4   # num of adjacent cells

# assuming the grid will always be square

for i in range(grid.shape[0]):
    for j in range(0, grid.shape[0], n):
        k = np.prod(grid[j:j+4, i])
        if k > product:
            product = k
            pos1 = [j, i]
            pos2 = [j+1, i]
            pos3 = [j+2, i]
            pos4 = [j+3, i]
        k = np.prod(t_grid[j:j+4, i])
        if k > product:
            product = k
            product = k
            pos1 = [i, j]
            pos2 = [i, j+1]
            pos3 = [i, j+2]
            pos4 = [i, j+3]

for i in range(grid.shape[0]-n+1):
    for j in range(grid.shape[0]-n+1):
        k = np.array([grid[i, j], grid[i+1, j+1], grid[i+2, j+2], grid[i+3, j+3]])
        k = np.prod(k)
        if k > product:
            product = k
            pos1 = [i, j]
            pos2 = [i+1, j+1]
            pos3 = [i+2, j+2]
            pos4 = [i+3, j+3]

for i in range(grid.shape[0]-n+1):
    for j in range(n-1, grid.shape[0]):
        k = np.array([grid[i, j], grid[i+1, j-1], grid[i+2, j-2], grid[i+3, j-3]])
        k = np.prod(k)
        if k > product:
            product = k   
            pos1 = [i, j]
            pos2 = [i+1, j-1]
            pos3 = [i+2, j-2]
            pos4 = [i+3, j-3] 

pos1 = tuple(pos1)
pos2 = tuple(pos2)
pos3 = tuple(pos3)
pos4 = tuple(pos4)

print(f'\nThe product of the marked numbers below is {product}')
print('\n')

for i in range(grid.shape[0]):
    for j in range(grid.shape[0]):
        if grid[i, j] < 10:
            print(' ', end='')
        if ((i, j) == pos1) or ((i, j) == pos2) or ((i, j) == pos3) or ((i, j) == pos4):
            cprint(grid[i, j], 'white', 'on_red', end=' ')
        else:
            print(grid[i, j], end=' ')
    print('', end='\n')

print('\n')