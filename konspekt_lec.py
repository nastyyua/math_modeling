print('Hello')

print(3+4)
print(3-4)
print(5*23)
print(348/2)
print(2**6)
print(7//2)
print(6%5)

s = 3+4
memory_id = id(s)
print(s, memory_id)

print(type(2))
print(type(2.8))
print(type('Boo!'))
print(type([1,3,6]))
print(type('True'))
print(type(None))

a = input('Введите число a:')
print(a)
print(type(a))

a = int(input('Введите число a:'))
print(type(a))

c = 'биба'
d = 'боба'
print(f'Здесь будут стоять {c} и {d}')

a = [1,3,6]
print(a[1])

b = [4, 7, 9]
c=a+b
print(c)

c.append ('Сказка')
print(c)

print ('Спасибо за лекцию!!')