def power(a, n):
    while n > 1:
        a += a
        n -= 1
    return a

print(power(2,7))