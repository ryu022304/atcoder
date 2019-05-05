n,m = map(int,input().split())
ab_list = [list(map(int,input().split())) for _ in range(m)]
dp = [[10**6 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 0

for a,b in ab_list:
    dp[a-1][b-1] = dp[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

for i in range(n):
    count = 0
    for j in range(n):
        if dp[i][j]==2:
            count += 1
    print(count)
