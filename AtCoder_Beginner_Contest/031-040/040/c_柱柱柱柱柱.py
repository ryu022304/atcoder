n = int(input())
a_list = list(map(int,input().split()))
dp = [10**9]*n
dp[0] = 0
dp[1] = abs(a_list[0]-a_list[1])
for i in range(2, n):
    dp[i] = min(dp[i-2]+abs(a_list[i-2]-a_list[i]), dp[i-1]+abs(a_list[i-1]-a_list[i]))
print(dp[-1])