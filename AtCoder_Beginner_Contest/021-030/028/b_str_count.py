import collections
s = list(input())
c = collections.Counter(s)
print('{} {} {} {} {} {}'.format(c['A'],c['B'],c['C'],c['D'],c['E'],c['F']))
