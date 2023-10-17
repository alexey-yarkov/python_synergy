x = int(input())
kol = 0
for i in range(1, x + 1):
    if x % i == 0:
        kol += 1
print(kol)
