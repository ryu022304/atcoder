import itertools
import collections
n,m = map(int,input().split())
ks_list = [list(map(int,input().split())) for _ in range(m)]
p_list = list(map(int,input().split()))

count = 0
tmp_list = []
for i,ks in enumerate(ks_list):
    k = ks[0]
    s = ks[1:]
    for val in [j for j in range(k+1) if j%2==p_list[i]]:
        tmp_list.extend(itertools.combinations(s, val))

print(tmp_list)