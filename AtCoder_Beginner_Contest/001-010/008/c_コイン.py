n = int(input())
c_list = [int(input()) for _ in range(n)]
res = 0
for i,c in enumerate(c_list):
    s = 0
    for j,c2 in enumerate(c_list):
        if c%c2 == 0 and i!=j:
            s += 1
    if s%2 == 1:
        res += 1/2
    else:
        res += (s+2)/(s*2+2)
print(res)
