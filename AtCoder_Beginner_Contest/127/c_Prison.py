n,m = map(int,input().split())
lr_list = list(list(map(int,input().split())) for _ in range(m))
res = [0]*(n+2)
for l,r in lr_list:
    res[l] += 1
    res[r+1] -= 1

for i in range(1,n+2):
    res[i] += res[i-1]

max_num = max(res)
if max_num == m:
    print(res.count(max_num))
else:
    print(0)