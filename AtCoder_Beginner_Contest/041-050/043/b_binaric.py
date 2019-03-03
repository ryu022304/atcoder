s_list = list(input())
res = []
for s in s_list:
    if s == 'B':
        if len(res)==0: continue
        res.pop(-1)
    else:
        res.append(s)
print(''.join(res))
