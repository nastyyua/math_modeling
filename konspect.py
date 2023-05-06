def mult_func(a):
    x = 3 * a
    return x 

def print_func(a):
    print(f'Моя print функция и {a}')

x0 = 10


def move(t):
    x = x0 * t
    return x


print(move(3))
# print(x) 

a = 'Good'

def my_func():
    a = 'Bad'
    print(a)

my_func()

# комплексные числа

a = 3
b = 4

z = complex(a, b)
print(z)

w = complex(b, a)

print(z + w)

#кортежи

a = 'hello'
print(a[0])

# a[0] = 'H' - нельяз изменить

t = [1, 4, 9]
print(t)
print(t[0])

# t[0] = 3 - нельзя изменить

#словари

d = {'a1':4, 4:'a1'}
print(d['a1'])

d['str'] = 'Good' #изменять можно
print(d)

#пример локального изменения глобальных обьектов

def changer(a, b):
    a = 2
    b[0] = 'Good' 

x = 10
L = [1,2]

changer(x, L)
print(x)
print(L)

L = [1, 2]

changer(x, L[:])
print(L)

def my_funnc(a=1, b=0):
    x = 3*a - b
    return x

print(my_funnc())
print(my_funnc(3,4))

def my_fuc(a, b = 0):
    x= 3*a- b
    return x

def my_fuunc(*args):
    x = 3 * args[0] - args[1]
    return x 

print(my_fuunc(3,4))

def my_nunc(**kwrgs):
    x = 3*kwrgs['obj_1'] - kwrgs['obj_2']
    return x 

print(my_nunc(obj_1 = 3, obj_2 = 4))