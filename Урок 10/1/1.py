pitomec = {}
name = input('Укажите кличку питомца ')
dannye = {}
dannye['Вид питомца'] = input('Укажите вид питомца ')
dannye['Возраст питомца'] = int(input('Укажите возраст питомца '))
dannye['Имя владельца'] = input('Укажите имя владельца питомца ')
pitomec[name] = dannye
print(pitomec)
print(pitomec[name]['Вид питомца'])
if pitomec[name]['Возраст питомца'] % 10 == 1 and pitomec[name]['Возраст питомца'] != 11:
    print('Это ', pitomec[name]['Вид питомца'], 'по кличке ', '"' + name
          + '". Возраст: ', pitomec[name]['Возраст питомца'], 'год. Имя владельца:', pitomec[name]['Имя владельца'])
elif pitomec[name]['Возраст питомца'] > 10 and pitomec[name]['Возраст питомца'] < 20:
    print('Это ', pitomec[name]['Вид питомца'], 'по кличке ', '"' + name
          + '". Возраст: ', pitomec[name]['Возраст питомца'], 'лет. Имя владельца:', pitomec[name]['Имя владельца'])
elif pitomec[name]['Возраст питомца'] % 10 >= 2 and pitomec[name]['Возраст питомца'] % 10 <= 4:
    print('Это ', pitomec[name]['Вид питомца'], 'по кличке ', '"' + name
          + '". Возраст: ', pitomec[name]['Возраст питомца'], 'года. Имя владельца:', pitomec[name]['Имя владельца'])
else:
    print('Это ', pitomec[name]['Вид питомца'], 'по кличке ', '"' + name
          + '". Возраст: ', pitomec[name]['Возраст питомца'], 'лет. Имя владельца:', pitomec[name]['Имя владельца'])
