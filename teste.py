import numpy as np
def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
a = list(result)
print(a)
print(type(a))
a = np.array(a)
print(a)
print(type(a))