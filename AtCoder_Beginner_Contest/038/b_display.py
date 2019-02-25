h1w1 = list(map(int,input().split()))
h2w2 = list(map(int,input().split()))
ok = False
for m in h1w1:
    if m in h2w2:
        ok = True
if ok:
    print('YES')
else:
    print('NO')
