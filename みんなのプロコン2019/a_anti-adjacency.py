N, K = map(int, input().split())
count = 0
for i in range(1,N+1):
    if i%2 == 0:
        pass
    else:
        count += 1

if count >= K:
    print('YES')
else:
    print('NO')
