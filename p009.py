# a + b + c = 1000
# a^2 + b^2 = c^2
# find a*b*c
# equacionando esse "sistema":
#   b = ((1000**2)/2 - 1000*a)/(1000 - a)
#   c = 1000 - (a + b)

k = 1000
stop = 500
a = 1
while a < 500: 
    b = ((k**2)/2 - k*a)/(k - a)
    c = k - (a + b)
    soma = a + b + c
    if b == int(b) and c == int(c) and soma == k:   # lol why did i do it like this?
        print(a, int(b), int(c))    # didnt need the int()
        print(int(a*b*c))   # here too
        a = stop + 1        # how to break for advanced pro masters!
    a += 1
