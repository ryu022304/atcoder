n = list(input())
indexes = [i for i,j in enumerate(n) if j == '1']
res = ['0']*3
for i in range(len(n)):
    if i in indexes:
        res[i]='9'
    else:
        res[i]='1'
print(''.join(res))
