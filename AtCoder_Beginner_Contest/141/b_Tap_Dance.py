s = list(input())

f = False

for i in range(len(s)):
    if i%2==0:
        if s[i]!='R' and s[i]!='U' and s[i]!='D':
            f = True
    else:
        if s[i]!='L' and s[i]!='U' and s[i]!='D':
            f = True
if f:
    print('No')
else:
    print('Yes')