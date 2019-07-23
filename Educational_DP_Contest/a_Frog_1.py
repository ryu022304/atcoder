n = int(input())
h_list = list(map(int,input().split()))
dp = [10**9]*n
dp[0] = 0
dp[1] = abs(h_list[0]-h_list[1])
for i in range(2, n):
    dp[i] = min(dp[i-1]+abs(h_list[i-1]-h_list[i]), dp[i-2]+abs(h_list[i-2]-h_list[i]))
print(dp[-1])