import numpy as np
n,m,c=map(int,input().split())
b_s = list(map(int,input().split()))
a_s = [list(map(int,input().split())) for _ in range(n)]
b_num = np.array(b_s)
count = 0
for a in a_s:
    a_num = np.array(a)
    res = np.dot(a_num,b_num)
    if res + c > 0:
        count += 1
print(count)
