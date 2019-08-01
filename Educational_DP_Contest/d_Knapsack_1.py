n,w = map(int,input().split())
wv_list = [map(int,input().split()) for _ in range(n)]
dp = [0]*(w+1)
for ww,vv in wv_list:
    for i in range(w, ww-1, -1):
        t = dp[i-ww] + vv
        dp[i] = max(dp[i], t)
print(max(dp))