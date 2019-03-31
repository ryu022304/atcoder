a,b = map(int,input().split())
if a <= b:
    print(a)
else:
    print(a-1 if a!=1 else 1)
