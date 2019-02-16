n = int(input())
a,b = map(int,input().split())
k = int(input())
pk = [int(i) for i in input().split()]

if a not in pk and b not in pk and (len(pk) == len(set(pk))):
    print('YES')
else:
    print('NO')
