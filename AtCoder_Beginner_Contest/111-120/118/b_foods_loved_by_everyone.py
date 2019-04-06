import collections
n,m = map(int,input().split())
k_list = []
for _ in [0]*n:
    k_list.extend([int(i) for i in input().split()[1:]])
col = collections.Counter(k_list)
count = 0
for k,v in col.most_common():
    if v == n:
        count += 1
print(count)
