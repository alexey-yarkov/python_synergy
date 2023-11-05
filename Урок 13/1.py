import random
n = int(input('Введите число столбцов '))
m = int(input('Введите число строк '))
a1 = [[random.randint(-10, 10) for _ in range(n)] for _ in range(m)]
a2 = [[random.randint(-10, 10) for _ in range(n)] for _ in range(m)]
print('Первая матрица')
for i in a1:
    print(i)
print('Вторая матрица')
for i in a2:
    print(i)
print('Сумма матриц')
a3 = [[0 for _ in range(n)] for _ in range(m)]
for i in range(n):
    for j in range(m):
        a3[j][i] = a1[j][i] + a2[j][i]
for i in a3:
    print(i)
