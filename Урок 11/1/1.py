def f(n):
    k = 1
    for i in range(1, n + 1):
        k *= i
    return k
m = f(int(input()))
a = []
for i in range(m, 0, -1):
    a.append(f(i))
print(a)
