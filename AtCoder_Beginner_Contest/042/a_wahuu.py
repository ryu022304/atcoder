import collections
abc = [int(i) for i in input().split()]
c = collections.Counter(abc)
if c[5] == 2 and c[7] == 1:
    print('YES')
else:
    print('NO')
