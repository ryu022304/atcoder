n,k = map(int,input().split())
score = []
res = 0

for i in range(1,n+1):
    count = 0
    while True:
        if i*2**count < k:
            count += 1
        else:
            score.append(count)
            break

for s in score:
    res += (1/n)*((1/2)**s)

print(res)