s = input()
n = 0
m = 0
l = ['a', 'e', 'i', 'o', 'u', 'y']
for i in range(len(s)):
    for j in range(len(l)):
        if l[j] == s[i]:
            m += 1
n = len(s) - m
print('Согласных ' + str(n), 'Гласных ' + str(m), sep='\n')
for i in range(len(l)):
    if l[i] in s:
        print('Букв ' + l[i] , s.count(l[i]))
    else:
        print('False')
