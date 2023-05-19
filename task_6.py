def construction(a,n):
    for i in range(1,1,n+1):
        x = a*i
        print(x)
        a += x
        print(a)
    return(a)

print(construction(2,7))