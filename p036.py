import time

def is_palindrome_str(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

start = time.time()

sum_palindromic = 0
for i in range(1, 1_000_000):
    if is_palindrome_str(str(i)) and is_palindrome_str(bin(i)[2:]):
            sum_palindromic += i

end = time.time()

print(sum_palindromic, f'{round(end-start, 2)}s')