import collections
s = list(input())
c = collections.Counter(s)
print(2*min(c['0'],c['1']))
