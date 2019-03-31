import collections
n = int(input())
s = list(input())
c = collections.Counter(s)
if c['R'] > c['B']:
    print('Yes')
else:
    print('No')
