s = input()
n = 0
m = 0
for i in range(len(s)):
    if (s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o'
        or s[i] == 'u' or s[i] == 'y'):
        m += 1
    else:
        n += 1
print('Согласных ' + str(n), 'Гласных ' + str(m), sep='\n')
if 'a' in s:
    print('Букв a ', s.count('a'))
else:
    print('False')
if 'e' in s:
    print('Букв e ', s.count('e'))
else:
    print('False')
if 'i' in s:
    print('Букв i ', s.count('i'))
else:
    print('False')
if 'o' in s:
    print('Букв o ', s.count('o'))
else:
    print('False')
if 'u' in s:
    print('Букв u ', s.count('u'))
else:
    print('False')
if 'y' in s:
    print('Букв y ', s.count('y'))
else:
    print('False')
