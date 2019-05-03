n = int(input())
ab_list = [list(map(int,input().split())) for _ in range(n)]
res = [0]*(10**6+2)

for a,b in ab_list:
    res[a] += 1
    res[b+1] -= 1

for i in range(1,1000002):
    res[i] += res[i-1]

print(max(res))
