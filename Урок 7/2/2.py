s1 = input()
s2 = s1[0]
chet = 0
for i in range(1, len(s1)):
    if s1[i - 1] == s1[i] and s1[i - 1] == ' ':
        chet += 1
    else:
        chet = 0
    if chet == 0:
        s2 += s1[i]
print(s2)
