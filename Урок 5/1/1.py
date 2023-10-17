n = int(input())
if n == 0:
    print('нулевое число')
elif n < 0 and abs(n) % 2 == 0:
    print('отрицательное четное число')
elif n < 0 and abs(n) % 2 == 1:
    print('отрицательное нечетное число')
elif n > 0 and n % 2 == 0:
    print('положительное четное число')
else:
    print('положительное нечетное число')
