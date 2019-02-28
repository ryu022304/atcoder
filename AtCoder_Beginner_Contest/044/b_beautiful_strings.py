import collections,sys
w = list(input())
c = collections.Counter(w)
for s,num in c.items():
    if num%2 != 0:
        print('No')
        sys.exit()
print('Yes')
