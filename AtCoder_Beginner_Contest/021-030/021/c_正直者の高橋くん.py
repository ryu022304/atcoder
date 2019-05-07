n = int(input())
a,b = map(int,input().split())
m = int(input())
xy_list = [list(map(int,input().split())) for _ in range(m)]
d = [[float("inf") for _ in range(n)] for _ in range(n)]

for i in range(n):
    d[i][i] = 0

for x,y in xy_list:
    d[x-1][y-1] = 1
    d[y-1][x-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

num_list = [0]*100
num_list[a-1] = 1

for i in range(n):
    for j in range(n):
        if d[a-1][j] != i:
            continue
        for k in range(n):
            if d[a-1][k]==i+1 and d[j][k]==1:
                num_list[k] += num_list[j]
                num_list[k] %= (10**9)+7

print(num_list[b-1])
