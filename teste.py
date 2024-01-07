a = [2, 2, 7]
b = [2, 5, 11]
a_simp = a[:]
for factor in a:
    if factor in b:
        a_simp.remove(factor)
        b.remove(factor)

print(a_simp)