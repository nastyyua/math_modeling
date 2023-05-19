def power(a, n):
    while n > 1:
        a += a
        n -= 1
    return a

print(power(2,7))

a = 2
n = 7

for i in range(1,1,n+1):
    x = a*i
    print(x)
    a += x
print(a)