# the number of routes to get to the bottom right corner of
# a N x N grid is simply the median (or max) of the 2*N th 
# line of Pascal's Triangle (counting from 0)

# that is the Combination(2n, n)

from math import factorial

grid_order = 20
print(int(factorial(grid_order*2)/((factorial(grid_order))**2)))