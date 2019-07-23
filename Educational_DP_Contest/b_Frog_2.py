n,k = map(int, input().split())
h_list = list(map(int, input().split()))
dp = [10**9]*n
dp[0] = 0
for i in range(1, n):
    for j in range(max(0,i-k),i):
        dp[i] = min(dp[i], dp[j] + abs(h_list[i]-h_list[j]))
print(dp[-1])