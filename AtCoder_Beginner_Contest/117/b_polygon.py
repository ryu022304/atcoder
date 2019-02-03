N = int(input())
L = [int(i) for i in input().split()]
L.sort()
max_line = L.pop(-1)
if max_line < sum(L):
    print('Yes')
else:
    print('No')
