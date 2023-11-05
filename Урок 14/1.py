def f(n, i = 0):
    if i == n:
        return []
    else:
        return [i] + f(n, i + 1)
print(*f(17), 'Конец списка')
