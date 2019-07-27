n = int(input())
dp = [10**9]*30000000
dp[0] = 0
pow6 = [6**i for i in range(10) if 6**i <= n]
pow9 = [9**i for i in range(10) if 9**i <= n]

for i in range(n):
    for p6 in pow6:
        dp[i+p6] = min(dp[i+p6], dp[i]+1)
    for p9 in pow9:
        dp[i+p9] = min(dp[i+p9], dp[i]+1)
#print(dp)
print(dp[n])