n,t = map(int,input().split())
ct_list = [list(map(int,input().split())) for _ in range(n)]
res = []
for c,time in ct_list:
    if time <= t:
        res.append(c)
print(min(res) if len(res)!=0 else 'TLE')
