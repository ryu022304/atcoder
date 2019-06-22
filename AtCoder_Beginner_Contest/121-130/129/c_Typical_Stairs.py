import sys
sys.setrecursionlimit(2000)

n,m = map(int,input().split())
a_list = [int(input()) for _ in range(m)]
count = 0
dp = [10**6]*n
def dfs(pos):
    global count
    print(pos, count)
    if pos >= n-1:
        count += 1
        return True
    for i in [1,2]:
        if pos+i in a_list:
            pass
        else:
            dfs(pos+i)
    return True

dfs(0)
print(count%1000000007)
