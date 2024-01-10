# a + b + c = 1000
# a^2 + b^2 = c^2
# find a*b*c
# equacionando esse "sistema":
#   b = ((1000**2)/2 - 1000*a)/(1000 - a)
#   c = 1000 - (a + b)

import time
import numpy as np

k = 1000
stop = 500
a = 1

start = time.time()

while a < 500: # for a > 500, b < 0 - that was pretty smart from old me
    b = ((k**2)/2 - k*a)/(k - a)
    c = k - (a + b)
    soma = a + b + c
    if b == int(b) and c == int(c) and soma == k:   # lol why did i do it like this?
        print(a, int(b), int(c))    # didnt need the int()
        print(int(a*b*c))   # here too
        a = stop + 1        # how to break for advanced pro masters!
    a += 1

print(f'first version: ({time.time()-start:4f}s)')

start = time.time()

a = np.arange(1, 500)
b = (((1000**2)/2 - 1000*a)/(1000 - a))
c = (1000 - (a + b))
b = np.where(b%1==0, b, 0)
c = np.where(c%1==0, c, 0)
soma = a + b + c
i = np.where(soma==1000)[0][0]
print(a[i], b[i], c[i], a[i]*b[i]*c[i])

print(f'new version: ({time.time()-start:4f}s)')