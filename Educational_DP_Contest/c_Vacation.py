n = int(input())
abc_list = [list(map(int,input().split())) for _ in range(n)]

dp = [[0,0,0] for _ in range(n)]
dp[0] = abc_list[0]

for i in range(1,n):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][j] = max(dp[i][j], dp[i-1][k]+abc_list[i][j])

print(max(dp[-1]))