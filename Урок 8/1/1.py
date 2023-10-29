l = []
n = int(input())
for i in range(n):
    l.append(int(input()))
for i in range(n - 1, -1, -1):
    print(l[i], end=' ')
