num_of_letters = {
    1 : 3,
    2 : 3,
    3 : 5,
    4 : 4,
    5 : 4,
    6 : 3,
    7 : 5,
    8 : 5,
    9 : 4,
    10 : 3,
    11 : 6,
    12 : 6,
    13 : 8,
    14 : 8,
    15 : 7,
    16 : 7,
    17 : 9,
    18 : 8,
    19 : 8,
    20 : 6,
    30 : 6,
    40 : 5,
    50 : 5,
    60 : 5,
    70 : 7,
    80 : 6,
    90 : 6,
    'hundred' : 7, 
    'thousand' : 8 
}

def get_udc(n):
    udc = []
    k = str(n)
    i = 0
    while i < len(k):
        if (len(k)-i == 2 and k[i] == '1'):
            a = int(k[i:i+2])
            if a != 0:
                udc.append(a)
            break
        a = int(k[i] + '0'*(len(k)-1-i))
        if a != 0:
            udc.append(a)
        i += 1
    return udc

def how_many_letters(number):
    digits = get_udc(number)
    s = 0
    for digit in digits:
        if digit >= 1000:
            h = digit // 1000
            s += num_of_letters[h] + num_of_letters['thousand']
            continue
        if digit >= 100:
            h = digit // 100
            s += num_of_letters[h] + num_of_letters['hundred']
            continue
        s += num_of_letters[digit]
    if (number % 100 != 0) and (number > 100):
        s += 3
    return s

s = 0
for number in range(1, 1001):
    s += how_many_letters(number)
print(s)