s = input()
chet = 0
for i in range(len(s) // 2):
    if s[i] == s[len(s) - 1 - i]:
        chet += 1
if chet == len(s) // 2:
    print('yes')
else:
    print('no')
