a,b,c = map(int,input().split())
count = 0
for i in range(1,101):
    if a*i % b == c:
        count += 1
if count > 0:
    print('YES')
else:
    print('NO')
