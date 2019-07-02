n,m = map(int,input().split())
ks_list = [list(map(int,input().split())) for _ in range(m)]
p_list = list(map(int,input().split()))

count = 0
for i in range(2**n):
    on = 0
    for j in range(m):
        cnt = 0
        for s in ks_list[j][1:]:
            if (i >> s-1)&1 == 1:
                cnt += 1
        if cnt%2 == p_list[j]:
            on += 1
    if on == m:
        count += 1
print(count)
