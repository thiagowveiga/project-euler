# 1
# 3² + (3²-2) + (3²-4) + (3²-6)
# 5² + (5²-4) + (5²-8) + (5²-12)
# 7² + (7²-6) + (7²-12) + (7²-18)
# ...

spiral_size = 1001

diag_sum = 1

i = 3
while i <= spiral_size:
    j = (i-1)/2
    diag_sum += (4 * (i**2)) - (12 * j)
    i += 2

print(diag_sum)