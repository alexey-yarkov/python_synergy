Mike = int(input('Введите сумму, которую может вложить Майкл '))
Ivan = int(input('Введите сумму, которую может вложить Иван '))
Min_x = int(input('Минимальная сумма инвестиций '))
if Mike >= Min_x and Ivan >= Min_x:
    print(2)
elif Mike >= Min_x:
    print('Mike')
elif Ivan >= Min_x:
    print('Ivan')
elif Mike + Ivan >= Min_x:
    print(1)
else:
    print(0)
