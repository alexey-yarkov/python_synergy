a = list(map(int, input().split()))
l = set(a)
k = 0
for x in l:
    for i in range(len(a)):
        if x == a[i]:
            k += 1
    if k > 1:
        print(x, 'YES')
    else:
        print(x, 'NO')
    k = 0
