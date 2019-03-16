import itertools
o = input()
e = input()
res = ''
for os,es in itertools.zip_longest(o,e):
    if os is not None:
        res += os
    if es is not None:
        res += es
print(res)
