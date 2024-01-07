def sum_of_squares(upto):
    sum = 0
    for i in range(upto + 1):
        sum += i**2
    return sum

def square_of_sum(upto):
    sum = 0
    for i in range(upto + 1):
        sum += i
    return sum**2

print(abs(sum_of_squares(100)-square_of_sum(100)))