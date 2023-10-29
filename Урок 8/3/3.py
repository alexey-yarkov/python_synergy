m = int(input())
n = int(input())
l = []
k = 0
x = 0
j = 1
for i in range(n):
    l.append(int(input()))
l.sort(reverse = True)
while len(l) > 0:
    if len(l) > 1:
        x = l[0] + l[j]
        if x > m and j < len(l) - 1:
            j += 1
        elif x > m and j == len(l) - 1:
            l.pop(0)
            j = 1
            k += 1
        else:
            l.pop(j)
            l.pop(0)
            j = 1
            k += 1
    else:
        k += 1
        l.pop(0)
print(k)
