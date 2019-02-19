n,a,b = map(int,input().split())
pos = [(input().split()) for _ in [0]*n]
res = 0
for s,d in pos:
    dir = int(d)
    if s == 'East':
        if dir < a:
            res += a
        elif a <= dir <= b:
            res += dir
        else:
            res += b
    else:
        if dir < a:
            res -= a
        elif a <= dir <= b:
            res -= dir
        else:
            res -= b
if res < 0:
    print('West',abs(res))
elif res > 0:
    print('East',res)
else:
    print(0)
