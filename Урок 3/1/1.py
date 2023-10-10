vid = input('Укажите вид питомца ')
god = int(input('Укажите возраст питомца '))
name = input('Укажите кличку питомца ')
if god % 10 == 1 and god != 11:
    print('Это ', vid, 'по кличке ', '"' + name + '". Возраст: ', god, 'год.')
elif god > 10 and god < 20:
    print('Это ', vid, 'по кличке  ', '"' + name + '". Возраст: ', god, 'лет.')
elif god % 10 >= 2 and god % 10 <= 4:
    print('Это ', vid, 'по кличке ', '"' + name + '". Возраст: ', god, 'года.')
else:
    print('Это ', vid, 'по кличке ', '"' + name + '". Возраст: ', god, 'лет.')
