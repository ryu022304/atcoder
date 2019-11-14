import itertools
n = int(input())
d_list = list(map(int,input().split()))
d_com = list(itertools.combinations(d_list,2))
res = 0
for a,b in d_com:
    res += a*b
print(res)