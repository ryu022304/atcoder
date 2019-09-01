import math
a,b = map(int, input().split())
if b <= a:
    print(1)
else:
    tmp = b-a
    print(1+math.ceil(tmp/(a-1)))