n,a,b,c = map(int,input().split())
l = [int(input()) for _ in range(n)]
INF = 10**9

def dfs(cur, a_tmp, b_tmp, c_tmp):
    if cur == n:
        return abs(a_tmp-a)+abs(b_tmp-b)+abs(c_tmp-c)-30 if min(a_tmp,b_tmp,c_tmp) > 0 else INF
    ret0 = dfs(cur+1, a_tmp, b_tmp, c_tmp)
    ret1 = dfs(cur+1, a_tmp+l[cur], b_tmp, c_tmp)+10
    ret2 = dfs(cur+1, a_tmp, b_tmp+l[cur], c_tmp)+10
    ret3 = dfs(cur+1, a_tmp, b_tmp, c_tmp+l[cur])+10
    return min(ret0, ret1, ret2, ret3)

print(dfs(0,0,0,0))
