import random
a = []
b = []
n = random.randint(1, 100001)
print('Количество элементов в первом списке', n)
for i in range(n):
    a.append(random.randint(1, 100001))
m = random.randint(1, 100)
print('Первый список', *a)
print('Количество элементов во втором списке', m)
for i in range(m):
    b.append(random.randint(1, 100))
print('Второй список', *b)
x = set(a)
y = set(b)
print('В каждом списке одновременно содержиться', len(x | y), 'чисел.')
