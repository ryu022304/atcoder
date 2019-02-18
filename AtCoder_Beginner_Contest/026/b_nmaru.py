import math
n = int(input())
rs = [int(input()) for _ in [0]*n]
rs.sort(reverse=True)
res = 0
for i,r in enumerate(rs):
    if i%2 == 0:
        res += math.pi*(r**2)
    else:
        res -= math.pi*(r**2)
print(res)
