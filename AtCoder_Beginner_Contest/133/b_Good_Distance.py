import itertools
import math
n,d = map(int,input().split())
x_list = [list(map(int,input().split())) for _ in range(n)]
x_c = itertools.combinations(x_list,2)
count = 0
for x in x_c:
    x1 = x[0]
    x2 = x[1]
    tmp = 0
    for i in range(d):
        tmp += (x1[i]-x2[i])**2
    tmp = math.sqrt(tmp)
    if tmp.is_integer():
        count += 1
print(count)