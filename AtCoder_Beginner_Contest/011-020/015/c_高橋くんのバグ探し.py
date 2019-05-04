n,k = map(int,input().split())
t_list = [list(map(int,input().split())) for _ in range(n)]

def dfs(question, value):
    if question == n:
        return value==0
    for i in range(k):
        if dfs(question+1, value^t_list[question][i]):
            return True
    return False

#print('Found' if dfs(0,0) else 'Nothing')
import itertools
f = False
print(*t_list)
for t in itertools.product(*t_list):
    print(t)
    tmp = 0
    for v in t:
        tmp = tmp^v
    if tmp == 0:
        f = True
        break
print('Found' if f else 'Nothing')
