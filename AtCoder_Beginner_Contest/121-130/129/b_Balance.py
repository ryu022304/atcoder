n = int(input())
w = list(map(int,input().split()))
res = []
for t in range(1,n):
    res.append(abs(sum(w[:t])-sum(w[t:])))
print(min(res))