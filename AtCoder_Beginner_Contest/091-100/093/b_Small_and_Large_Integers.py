import math
a,b,k = map(int, input().split())
res = []
if 2*k > b-a:
    k = math.ceil((b-a)/2)+1
for i in range(k):
    res.append(a+i)
    res.append(b-i)

for s in sorted(set(res)):
    print(s)
