import collections
n = int(input())
s_list = [input() for _ in range(n)]
m = int(input())
t_list = [input() for _ in range(m)]

cs = dict(collections.Counter(s_list))
ct = dict(collections.Counter(t_list))

count_list = []
for k,v in cs.items():
    if k in ct:
        if ct[k] < v:
            count_list.append(v-ct[k])
    else:
        count_list.append(v)

print(max(count_list) if len(count_list)!= 0 else 0)
