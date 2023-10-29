l1 = []
l2 = []
n = int(input())
for i in range(n):
    l1.append(int(input()))
l2.append(l1[n - 1])
for i in range(n - 1):
    l2.append(l1[i])
print(l2)
