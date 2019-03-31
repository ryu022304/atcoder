d,n = map(int,input().split())
if n == 100:
    n = 101
if d == 0:
    print(1*n)
elif d == 1:
    print(100*n)
elif d == 2:
    print(10000*n)
